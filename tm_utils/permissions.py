from rest_framework import permissions

class BaseObjectPermissionValidator:
    def __init__(self, request, view, obj):
        self.request = request
        self.view = view
        self.obj = obj
        self.authorized_company_id = AccessControlService.get_company_id(request)
        self.object_permission_type = getattr(view, "object_permission_type", None)

    def validate(self):
        return False

class IsAuthenticated(permissions.BasePermission):
    """
    Global permission check for login user access
    """

    exception = ["post_auth", "post_user", "post_jwt_auth", "get_RatingFlowView", "get_rating_question", "get_job"]
    object_permission_validator = BaseObjectPermissionValidator

    def has_permission(self, request, view):
        return True