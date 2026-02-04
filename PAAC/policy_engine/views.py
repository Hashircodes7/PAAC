from django.shortcuts import render
from policy_engine.models import Policy
from rest_framework.pagination import PageNumberPagination
from policy_engine.serializers import Policy_Serializer
from policy_engine.permissions import Policy_Permissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

class Pagination_Class(PageNumberPagination):
    page_size=10

class Create_Policy_View(APIView):

    permission_classes=[IsAuthenticated,Policy_Permissions]

    def post(self,request):
        serializer=Policy_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Update_Policy_View(APIView):

    permission_classes=[IsAuthenticated,Policy_Permissions]
    
    def patch(self,request,pid):
        pobj=get_object_or_404(Policy,id=pid)
        serializer=Policy_Serializer(pobj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Delete_Policy_View(APIView):

    permission_classes=[IsAuthenticated,Policy_Permissions]
    
    def delete(self,request,pid):
        pobj=get_object_or_404(Policy,id=pid)
        pobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class List_Policies(APIView):

    permission_classes=[IsAuthenticated,Policy_Permissions]
    
    def get(self,request):
        pobj=Policy.objects.all()
        paginator=Pagination_Class()
        paginate_qs=paginator.paginate_queryset(pobj,request)
        serializer=Policy_Serializer(paginate_qs,many=True)
        return paginator.get_paginated_response(serializer.data)
    
class Get_Spec_Policy(APIView):

    permission_classes=[IsAuthenticated,Policy_Permissions]

    def get(self,request,pid):
        pobj=get_object_or_404(Policy,id=pid)
        serializer=Policy_Serializer(pobj)
        return Response(serializer.data,status=status.HTTP_200_OK)