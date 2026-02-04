from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from audit_log.serializers import Audit_Serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from audit_log.models import Audit
from audit_log.permissions import Audit_Permissions

# Create your views here.

class Audit_Pagination(PageNumberPagination):
    page_size=6

class Audit_List_View(APIView):

    permission_classes=[IsAuthenticated,Audit_Permissions]

    def get(self,request):
        queryset=Audit.objects.all()
        paginator=Audit_Pagination()
        paginator_qs=paginator.paginate_queryset(queryset,request)
        serializer=Audit_Serializer(paginator_qs,many=True)
        return paginator.get_paginated_response(serializer.data)
    
class Policy_Audit_View(APIView):

    permission_classes=[IsAuthenticated,Audit_Permissions]

    def get(self,request,pid):
        policy_qs=Audit.objects.select_related('decision__policy_used').filter(decision__policy_used__id=pid).order_by('-audit_time')
        serializer=Audit_Serializer(policy_qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class User_Audit_View(APIView):

    permission_classes=[IsAuthenticated,Audit_Permissions]

    def get(self,request,uid):
        user_qs=Audit.objects.select_related('decision__user').filter(decision__user__id=uid)
        serializer=Audit_Serializer(user_qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)