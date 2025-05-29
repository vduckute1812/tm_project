from authtools.models import User
from tm_utils.serializers.abstract import BaseSerializer


class RegisterUserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}
