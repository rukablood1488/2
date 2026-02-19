from django.db import models
from django.contrib.auth.models import User


class TaskStatus(models.TextChoices):
    IN_PROGRESS = 'in_progress', 'In Progress'
    DONE = 'done', 'Done'
    POSTPONED = 'postponed', 'Postponed'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.IN_PROGRESS
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        return f"{self.title} - {self.status}"
