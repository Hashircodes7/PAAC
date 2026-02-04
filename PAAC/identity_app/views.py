from identity_app.serializers import User_Serializer
from rest_framework.permissions import IsAuthenticated
from identity_app.permissions import User_Permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from identity_app.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

class Standard_Pagination(PageNumberPagination):
    page_size=10


#Intentionally used apiviews to showcase request-response concepts 


class Create_User_View(APIView):

    permission_classes=[IsAuthenticated,User_Permissions]
    def post(self,request):
        serializer=User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Update_User_View(APIView):

    permission_classes=[IsAuthenticated,User_Permissions]

    def patch(self,request,uid):

        obj=get_object_or_404(User,id=uid)
        self.check_object_permissions(request, obj)
        serializer=User_Serializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Delete_User_View(APIView):
    permission_classes=[IsAuthenticated,User_Permissions]

    def delete(self,request,uid):
        obj=get_object_or_404(User,id=uid)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class Get_Users(APIView):
    
    permission_classes=[IsAuthenticated,User_Permissions]
    def get(self,request):
        qs=User.objects.all()
        paginator=Standard_Pagination()
        paginate_qs=paginator.paginate_queryset(
            qs,request
        )
        serializer=User_Serializer(paginate_qs,many=True)
        return paginator.get_paginated_response(serializer.data)
    
class Get_Spec_User(APIView):

    permission_classes=[IsAuthenticated,User_Permissions]
    def get(self,request,uid):
        obj=get_object_or_404(User,id=uid)
        serializer=User_Serializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
