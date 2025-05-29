from datetime import datetime
from typing import List

from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication

from tm_user.constants.toastmaster import VerificationType
from tm_user.models.register_form import TMRegisterForm
from tm_utils.exceptions.tm_user import TokenExpired, TokenRequired, InvalidToken


class GuestAuthentication(BaseAuthentication):
    authenticate_token = "tm-guest-token"

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
            login = TMRegisterForm.objects.get(token=token, verification_type=VerificationType.NEW_GUEST)
        except TMRegisterForm.DoesNotExist:
            raise
        if self.token_expired(login):
            raise TokenExpired()
        return login.user, login.token

    def authenticate_header(self, request):
        return self.authenticate_token

    @staticmethod
    def validate_token(auth: List[str]) -> str:
        if len(auth) == 1:
            raise TokenRequired()
        elif len(auth) > 2:
            raise InvalidToken()
        try:
            token = auth[1]
        except UnicodeError:
            raise InvalidToken()
        return token

    @staticmethod
    def token_expired(token):
        return token.token_expired_at < datetime.now()
