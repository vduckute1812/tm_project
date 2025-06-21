from rest_framework import serializers

class AuthenticationTokenSerializer(serializers.Serializer):
    """
    Serializer for the authentication token.
    """
    username = serializers.CharField(required=True, max_length=32)
    password = serializers.CharField(required=True, max_length=32, write_only=True)

    def validate(self, attrs):
        """
        Validate the username and password.
        """
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        # Additional validation logic can be added here if needed

        return attrs