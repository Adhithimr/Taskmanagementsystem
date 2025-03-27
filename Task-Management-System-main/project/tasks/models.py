from django.db import models
from django.utils import timezone

# Create your models here.
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
