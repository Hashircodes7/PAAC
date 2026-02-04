from simulation_mode.serializers import Simulation_Serializer
from rest_framework.permissions import IsAuthenticated
from .permissions import Simulation_Permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from simulation_mode.models import Simulation
from decision_engine.logic import Evaluate_Policy
from decision_engine.models import Decision
from django.shortcuts import get_object_or_404

# Create your views here.
class Simulation_Pagination(PageNumberPagination):
    page_size=6


class Simulate_Decision_View(APIView):

    permission_classes=[IsAuthenticated,Simulation_Permissions]

    def post(self, request):
        serializer = Simulation_Serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        simulation = serializer.save()

        subject_user = simulation.user_subject
        action = request.data.get('action')
        resource = request.data.get('resource')

        decision_result = Evaluate_Policy(
            subject_user,
            action,
            resource
        )

        simulation.decision = Decision.objects.create(
            user=subject_user,
            result=decision_result['result'],
            reason=decision_result['reason'],
            policy_used=decision_result.get('policy') 
        )

        simulation.save()

        return Response(
            Simulation_Serializer(simulation).data,
            status=status.HTTP_201_CREATED )
       

class List_Simulation_View(APIView):

    permission_classes=[IsAuthenticated,Simulation_Permissions]

    def get(self,request):

        user=request.user

        if user.role in ['ceo','auditor']:
            qs = Simulation.objects.all().select_related('created_by', 'user_subject', 'decision__policy_used')
        elif user.role == 'manager':
            qs=Simulation.objects.filter( created_by = user) | Simulation.objects.filter( user_subject__department=user.department )
        else:
            qs=Simulation.objects.none()

        paginator=Simulation_Pagination()
        paginator_qs=paginator.paginate_queryset(qs,request)
        serializer=Simulation_Serializer(paginator_qs,many=True)
        return paginator.get_paginated_response(serializer.data)

class Specific_Simulation_View(APIView):

    permission_classes=[IsAuthenticated,Simulation_Permissions]

    def get(self,request,sid):
        user=request.user
        simulation=get_object_or_404(Simulation,id=sid)
   
        if user.role in ['ceo','auditor']:
            pass
        elif user.role == 'manager':
            if not (simulation.created_by == user or simulation.user_subject.department == user.department):
                return Response ({"detail": "not allowed"},status=status.HTTP_403_FORBIDDEN)
            
        else:
            return Response({"detail":"not allowed"},status=status.HTTP_403_FORBIDDEN)


        serializer=Simulation_Serializer(simulation)
        return Response(serializer.data,status=status.HTTP_200_OK)