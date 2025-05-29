from authtools.models import User
from rest_framework import serializers

from tm_user.services.user import UserService


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return UserService.save(data=validated_data)
