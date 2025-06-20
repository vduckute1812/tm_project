import jwt
from django.conf import settings
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

class BaseToken:
    expire_minutes = 60  # default expiry time

    def encode(self, payload: dict, expire_minutes: int = None) -> str:
        """
        Encode the payload into a JWT token string.
        :param payload: The data to encode in the token.
        :param expire_minutes: Minutes until the token expires.
        :return: Encoded token string.
        """
        if expire_minutes is None:
            expire_minutes = self.expire_minutes
        payload = payload.copy()
        payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        return jwt.encode(payload, self.__secret_key, algorithm=self.__algorithm)

    def decode(self, token: str) -> Dict[str, Any]:
        """
        Decode a JWT token string.
        :param token: The encoded token string.
        :return: Decoded payload.
        :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
        """
        return jwt.decode(token, self.__secret_key, algorithms=[self.__algorithm])

    @property
    def __secret_key(self) -> str:
        return settings.SECRET_KEY

    @property
    def __algorithm(self) -> str:
        return "HS256"