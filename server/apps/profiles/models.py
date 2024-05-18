from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True)
    