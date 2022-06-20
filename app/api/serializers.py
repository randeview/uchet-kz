from rest_framework import serializers
from app.models import Todo
from app.tasks import send_email_task


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'finished')


class TodoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'deadline', 'finished')

    def create(self, validated_data):
        if validated_data.get('finished'):
            raise serializers.ValidationError('New created task cannot be completed!')

        return super(TodoDetailsSerializer, self).create(validated_data)


class TodoUpdateSerializer(TodoDetailsSerializer):
    def save(self, **kwargs):
        user = self.context['user']
        finished = self.validated_data.get('finished')

        if finished and self.instance.finished != finished:
            send_email_task.delay(user.email)

        return super(TodoUpdateSerializer, self).save(**kwargs)
