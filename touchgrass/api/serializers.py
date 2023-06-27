from rest_framework.serializers import ModelSerializer, EmailField, CharField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from api.models import Post, AdminMessage, Profile

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AdminMessageSerializer(ModelSerializer):
    class Meta:
        model = AdminMessage
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

        