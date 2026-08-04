from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source ='owner.username')
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'status_display', 'priority','priority_display', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['owner']