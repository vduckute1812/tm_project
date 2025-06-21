from datetime import datetime
from typing import List

from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication

from tm_user.constants.toastmaster import VerificationType
from tm_user.models.user_auth import TMUserAuth
from tm_utils.exceptions.tm_user import TokenExpired, TokenRequired, InvalidToken


class GuestAuthentication(BaseAuthentication):
    """Authentication class for guest users in the Toastmaster application.
    This class handles the authentication of guest users using a token-based system.
    It checks the provided token against the database and verifies its validity.
    If the token is valid and not expired, it returns the associated user and token.
    If the token is invalid or expired, it raises appropriate exceptions.
    """
    authenticate_token = "tm-guest-token"   # It is recommended to use a constant for the token type
 
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()
        auth_type = auth and auth[0].decode("utf-8").lower()
        
        if auth_type == self.authenticate_token:
            token = self.validate_token(auth=auth)
            return self.authenticate_credentials(token)
        else:
            return super().authenticate(request)

    def authenticate_credentials(self, token):
        try:
            login = TMUserAuth.objects.get(token=token, verification_type=VerificationType.NEW_GUEST)
        except TMUserAuth.DoesNotExist:
            raise InvalidToken()
        if self.token_expired(login):
            raise TokenExpired()
        return login.user, login.token

    def authenticate_header(self, request):
        return self.authenticate_token

    @staticmethod
    def validate_token(auth: List[str]) -> str:
        if len(auth) == 1:
            raise TokenRequired()
        elif not auth or len(auth) > 2:
            raise InvalidToken()
        return auth[1]

    @staticmethod
    def token_expired(token):
        return token.token_expired_at < datetime.now()
