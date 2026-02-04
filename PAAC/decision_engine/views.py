from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from decision_engine.serializers import Decision_Serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from decision_engine.models import Decision
from rest_framework.views import APIView
from decision_engine.logic import Evaluate_Policy,Evaluate_User
from audit_log.models import Audit
# Create your views here.
class Decision_Pagination(PageNumberPagination):
    page_size=5

class Create_Decision_View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
       
        serializer = Decision_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        action = serializer.validated_data['action']
        resource = serializer.validated_data['resource']

        
        user_obj = Evaluate_User(request.user)
        policy_obj = Evaluate_Policy(request.user, action, resource)

       
        decision_obj = Decision.objects.create(
            user=request.user,
            policy_used=policy_obj.get('policy', None),
            result=policy_obj.get('result'),
            reason=policy_obj.get('reason'),
            action=action,
            resource=resource
        )

       
        Audit.objects.create(decision=decision_obj)

       
        output_serializer = Decision_Serializer(decision_obj, context={'user_obj': user_obj, 'policy_obj': policy_obj})

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class Specific_Decision_View(APIView):
 
    permission_classes=[IsAuthenticated]

    def get(self,request,did):
        dec_obj=get_object_or_404(Decision,id=did,user=request.user)
        serializer=Decision_Serializer(dec_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class List_Decisions_View(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):
        query_set=Decision.objects.filter(user=request.user).order_by('-evaluated_at').select_related('user','policy_used')
        paginator=Decision_Pagination()
        paginate_qs=paginator.paginate_queryset(query_set,request)
        serializer=Decision_Serializer(paginate_qs,many=True)
        return paginator.get_paginated_response(serializer.data)