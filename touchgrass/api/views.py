from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import PostSerializer, AdminMessageSerializer, ProfileSerializer
from api.models import Post, AdminMessage, Profile


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)


@api_view(['GET'])
def getProfile(request):
    profile_owner = request.profile_owner
    profile = Profile.objects.get(owner=profile_owner)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAdminMessages(request):
    user = request.user
    messages = user.adminmessage_set.all()
    serializer = AdminMessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendAdminMessage(request):
    user = request.user
    body = request.body
    message = AdminMessage(user=user, body=body)
    message.save()
    return