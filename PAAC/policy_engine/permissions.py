from rest_framework.permissions import BasePermission

class Policy_Permissions(BasePermission):
    def has_permission(self, request, view):
        
        if request.user.role  == 'ceo':
            return True
            
        return False