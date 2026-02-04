from rest_framework.permissions import BasePermission

class Audit_Permissions(BasePermission):
    def has_permission(self, request, view):
        
        if request.user.role in ['auditor','ceo']:
            return True
        return False