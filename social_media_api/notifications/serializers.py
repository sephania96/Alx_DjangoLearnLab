from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_object_id = serializers.IntegerField(write_only=True)
    target_model = serializers.CharField(write_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target', 'target_object_id', 'target_model', 'timestamp']
        read_only_fields = ['id', 'recipient', 'actor', 'actor_username', 'target', 'timestamp']