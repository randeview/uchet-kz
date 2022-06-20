from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from users.models import UserProfile


class AuthLoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.AuthLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class AuthLogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "logout success"}, status=200)
        except UserProfile.DoesNotExist:
            return Response({"message": "user unauthorized"}, status=401)
        except UserProfile.auth_token.RelatedObjectDoesNotExist:
            return Response({"message": "user unauthorized"}, status=401)
