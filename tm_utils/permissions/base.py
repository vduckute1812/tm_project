from rest_framework import permissions
from tm_utils.services.utils.access_control import AccessControlService

class BaseObjectPermissionValidator:
    def __init__(self, request, view, obj):
        self.request = request
        self.view = view
        self.obj = obj
        self.authorized_company_id = AccessControlService.get_club_id(request)

    def validate(self):
        return False

class IsAuthenticated(permissions.BasePermission):
    """
    Global permission check for login user access
    """

    def has_permission(self, request, view):
        return True
