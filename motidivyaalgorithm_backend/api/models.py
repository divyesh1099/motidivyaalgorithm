from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.title