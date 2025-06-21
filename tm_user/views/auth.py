from django.http import HttpResponse

from tm_user.serializers.auth_token import AuthenticationTokenSerializer
from tm_user.throttles.auth import UserAuthThrottle
from tm_utils.mixins.view import GenericViewMixin


# Create your views here.

class AuthViewSet(GenericViewMixin):
    serializer_class = AuthenticationTokenSerializer
    throttle_classes = (UserAuthThrottle,)

    def create(self, request):
        """
        @api {post} /auth Login
        @apiName Login
        @apiGroup Auth
        @apiDescription Success login will return response with token, which will be included in HTTP HEADER for further api request

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: Handle to create new auth object and check expire status
        is_expired_password = False
        if is_expired_password:
            return HttpResponse(
                "Your password has expired. Please change your password to continue.",
                status=403,
            )
        else:
            # Handle login successfully
            pass
        return HttpResponse(
            "Login successful. Token will be included in HTTP HEADER for further API requests.",
            status=200,
        )