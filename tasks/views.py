from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_email_notification_when_task_created
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import os
class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'priority', 'status']
    
    recipent_email = os.environ.get('EMAIL_HOST_USER')

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(owner=self.request.user)
        send_email_notification_when_task_created.delay(serializer.validated_data.get('title'), self.recipent_email)
        