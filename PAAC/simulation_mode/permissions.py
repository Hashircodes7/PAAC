from rest_framework.permissions import BasePermission

class Simulation_Permissions(BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.role in ['ceo', 'auditor','manager']:
            return True


        return False
