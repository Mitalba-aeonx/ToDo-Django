from django.db import models
from django.contrib.auth.models import User


priority_choices = [
    ('l','Low'),
    ('m','Medium'),
    ('h','High'),
]

status_choices = [
    ('t','Completed'),
    ('p','Pending')
]
# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    is_completed = models.CharField(max_length=20,choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    priority = models.CharField(max_length=20,choices=priority_choices)