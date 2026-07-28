from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'TODO', 'To do'
        IN_PROGRESS = 'IN_PROGRESS', 'In progress'
        DONE = 'DONE', 'Done'

    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.title} ({self.status})"