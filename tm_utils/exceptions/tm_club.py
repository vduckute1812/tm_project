from rest_framework.exceptions import APIException


class TokenExpired(APIException):
    status_code = 401
    default_detail = "Division not be found or has been deleted"
