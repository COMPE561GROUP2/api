from rest_framework.serializers import ModelSerializer
from api.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AdminMessageSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'