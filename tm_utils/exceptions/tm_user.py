from rest_framework.exceptions import APIException


class TokenExpired(APIException):
    status_code = 401
    default_detail = "Token expired"

class TokenRequired(APIException):
    status_code = 401
    default_detail = "Token required"

class InvalidToken(APIException):
    status_code = 401
    default_detail = "Invalid token"