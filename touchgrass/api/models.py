from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = User()
    bio = models.TextField(max_length=512)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

class AdminMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()