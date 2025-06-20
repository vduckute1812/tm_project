import jwt
from django.conf import settings

class BaseToken:


    def encode(self, payload: dict) -> str:
        """
        Encode the payload into a token string.
        :param payload: The data to encode in the token.
        :return: Encoded token string.
        """
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    

    @property
    def _secret_key(self) -> str:
        """
        Get the secret key used for encoding and decoding tokens.
        :return: Secret key string.
        """
        return settings.SECRET_KEY