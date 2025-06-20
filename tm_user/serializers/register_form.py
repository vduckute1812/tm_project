import re

from authtools.models import User
from rest_framework import serializers

# This form serializer is used to handle user registration data.
class RegisterFormSerializer(serializers.Serializer):
    registered_date = serializers.DateTimeField(read_only=True)
    email = serializers.CharField(required=True, max_length=32)
    # The field will NOT be included in API responses
    password = serializers.CharField(required=True, max_length=32, write_only=True)

    # Validate the email to ensure it is unique
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    # Validate the password to ensure it meets certain criteria
    def validate_password(self, value):
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value

    # When an admin approve the form
    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
