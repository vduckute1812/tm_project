from rest_framework.throttling import UserRateThrottle

class UserAuthThrottle(UserRateThrottle):
    """
    Throttle for user authentication requests.
    This throttle is used to limit the number of authentication attempts
    a user can make within a specified time period.
    """
    scope = 'user_auth_requests'

    def allow_request(self, request, view):
        """
        Check if the user is allowed to make an authentication request.
        """
        # Logic to check if the user has exceeded the rate limit
        # This would typically involve checking a cache or database
        if not request.user.is_authenticated:
            # If the user is not authenticated, apply the throttle
            return super().allow_request(request, view)
        # If the user is authenticated, allow the request without throttling
        return True
