from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_task_creation_notification

class TaskViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
   
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(owner=self.request.user)
        send_task_creation_notification.delay(serializer.validated_data.get('priority'), serializer.validated_data.get('title'))
        