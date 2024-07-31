from django.db import models

class TaskAllocA(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'Completed', 'Completed'
        PENDING = 'Pending', 'Pending'

    task = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # This field auto-updates with changes
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return self.task
