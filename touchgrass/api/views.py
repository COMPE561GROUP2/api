from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import PostSerializer, AdminMessageSerializer, ProfileSerializer
from api.models import Post, AdminMessage, Profile
from django.contrib.auth.models import User

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


@api_view(['POST'])
def getProfile(request):
    username = request.data['user']
    
    try:
        owner = User.objects.get(username=username)
        profile = Profile.objects.get(user_id=owner.pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addProfile(request):
    username = request.data['user']
    user = User.objects.get(username=username)
    profile_exists = Profile.objects.filter(pk=user.pk).exists()

    if not profile_exists:

        profile = Profile(
            user_id=user,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            bio=None
        )
        
        profile.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_409_CONFLICT)


@api_view(['PUT'])
def editProfile(request):
    username = request.data['user']
    user = User.objects.get(username=username)
    profile_exists = Profile.objects.filter(pk=user.pk).exists()

    if profile_exists:
        profile = Profile.objects.filter(pk=user.pk)
        

    else:
        return Response(status=status.HTTP_409_CONFLICT)


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