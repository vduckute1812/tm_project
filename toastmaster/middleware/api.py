from toastmaster.settings import tm_local
from django.utils.deprecation import MiddlewareMixin

class APIMiddleware(MiddlewareMixin):
    """
    Middleware to handle API requests and responses.
    This middleware can be used to log requests, handle exceptions,
    or modify the request/response objects.
    
    Example usage:
        Add 'toastmaster.middleware.api.APIMiddleware' to MIDDLEWARE in settings.py.
    """

    def process_request(self, request):
        """
        Process the incoming request before it reaches the view.
        This method can be used to log requests or modify request data.
        """
        # Example: Log the request path
        tm_local.request = request
        tm_local.access_control = {}
        print(f"Request path: {request.path}")

    def process_response(self, request, response):
        """
        Process the response before it is sent to the client.
        This method can be used to log responses or modify response data.
        """
        # Example: Log the response status code
        print(f"Response status code: {response.status_code}")
        return response
    