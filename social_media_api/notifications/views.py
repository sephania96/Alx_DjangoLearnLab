from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.contenttypes.models import ContentType

class CreateNotificationView(APIView):
    def post(self, request, verb, target_id, target_model):
        recipient = request.user
        actor = request.user
        target_content_type = ContentType.objects.get(model=target_model)
        target_object_id = target_id
        notification = Notification.objects.create(recipient=recipient, actor=actor, verb=verb, target_content_type=target_content_type, target_object_id=target_object_id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

class GetNotificationsView(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
