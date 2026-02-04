from rest_framework.permissions import BasePermission

class User_Permissions(BasePermission):

    def has_permission(self, request, view):
       
        if not request.user.is_authenticated:
            return False

       
        allowed_methods = ['GET', 'POST', 'PATCH', 'DELETE']
        if request.method not in allowed_methods:
            return False

       
        if request.user.role == 'ceo':
            return True

       
        if request.user.role == 'manager':
   
            if request.method in ['GET','POST', 'PUT', 'PATCH']:
                return True

          
            if request.method == 'DELETE':
                return False

        return False
    
    def has_object_permission(self, request, view, obj):
       
        if request.user.role == 'ceo':
            return True

       
        if request.user.role == 'manager':
            if request.method in ['PUT', 'PATCH','DELETE']:
                if obj.department == request.user.department and obj.role in ['intern', 'employee']:
                    return True
            if request.method == 'GET':
                return True
            return False

        return False
