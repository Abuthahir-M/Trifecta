from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRIORITY_CHOICES = [
        ('High Priority', 'High Priority'),
        ('Medium Priority', 'Medium Priority'),
        ('Low Priority', 'Low Priority'),
    ]

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=500)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name
# Create your models here.
