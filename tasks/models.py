from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Status(models.IntegerChoices):
        TODO = 1, 'To do'
        IN_PROGRESS = 2, 'In progress'
        DONE = 3, 'Done'

    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.TODO)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.title} ({self.status})"