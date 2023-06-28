from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.TextField(max_length=150, null=True)
    first_name = models.TextField(max_length=150, null=True)
    last_name = models.TextField(max_length=150, null=True)

    email = models.TextField(max_length=150, null=True)

    bio = models.TextField(max_length=512, null=True)
    #following = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

class AdminMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()