from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)  # Task title
    category = models.CharField(max_length=50, blank=True, null=True)  # Category/label
    completed = models.BooleanField(default=False)  # Completion status
    start_time = models.DateTimeField(blank=True, null=True)  # Task start time
    end_time = models.DateTimeField(blank=True, null=True)  # Task end time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Task owner

    def __str__(self):
        return self.title
