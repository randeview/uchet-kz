from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from app.models import Todo
from . import serializers


class TodoViewSet(GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_serializer_class(self, action=None):
        if self.action in ['retrieve', 'create']:
            return serializers.TodoDetailsSerializer

        if self.action in ['update', 'partial_update']:
            return serializers.TodoUpdateSerializer

        return super().get_serializer_class()
