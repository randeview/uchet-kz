from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import UserProfile


class AuthLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError("email is required")

        if password is None:
            raise serializers.ValidationError("password is required")

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("user not found")

        if not user.check_password(password):
            raise serializers.ValidationError("wrong password")

        token = Token.objects.get_or_create(user=user)[0]

        return {"email": email, "token": token}

