from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()


class AdminMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()