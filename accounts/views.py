from builtins import print
import imp
from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Profile
from .serializers import ProfileSerializer, CreateRandomIdSerializer, ChangeUserInfoSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from latte.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import serializers
from django.contrib.auth import authenticate





    
class ProfileAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # Response({"uielements": result})
    def put(self, request, id) :
      if id is None:
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
      else :
        user_profile = Profile.objects.get(user_id = id)
        user_profile_serializer = ProfileSerializer(user_profile, data = request.data)
        if user_profile_serializer.is_valid():
          user_profile_serializer.save()
          return Response(user_profile_serializer.data, status=status.HTTP_200_OK)
        else :
          return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id) :
      if id is None:
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
      else :
        user_profile = Profile.objects.get(user_id = id)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class CreateRandomIdAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = CreateRandomIdSerializer

    def post(self, request) :
      queryset = list(User.objects.all())[-1]
      new_id = queryset.id + 1
      random_username = "random_username" + str(new_id)
      data = {'username' : random_username, 'password': 'changeme', 'email': 'changeme@latte.com'}
      # new_user = User.objects.create_user(username=random_username, password='changeme', email='changeme@latte.com')
      serializer = CreateRandomIdSerializer(data = data)
      if serializer.is_valid():
        serializer.save()
        user = User.objects.get(id = new_id)
        token = Token.objects.create(user=user)
        return Response(
          {"User" : serializer.data, "Token" : token.key}, status=201)
      else :
        return Response(serializer.errors, status=400)

class ChangeUserInfoAPIView(APIView) :
    serializer_class = ChangeUserInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def put(self, request, id) :
      if id is None:
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
      else :
        user = User.objects.get(id = id)
        data = request.data
        data._mutable = True
        data['is_active'] = True
        data._mutable = False
        change_user_info_serializer = ChangeUserInfoSerializer(user, data = data)
        if change_user_info_serializer.is_valid():
          change_user_info_serializer.save()
          user.set_password(change_user_info_serializer.data.get("password"))
          user.save()
          return Response(change_user_info_serializer.data, status=201)
        else :
          return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginAPIView(APIView) :
  queryset = User.objects.all()
  serializer_class = LoginSerializer
  
  def post(self, request) :
    print(request.data)
    # username = request.POST.get("username", None)
    # password = request.POST.get("password", None)
    username = request.data["username"]
    password = request.data["password"]
    try :
      user = authenticate(username=username, password=password)
      print(user)
      if user is None :
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
      else :
        data = request.data
        # data._mutable = True
        # data._mutable = False 
        token = Token.objects.get(user_id = user.id)
        serializer = LoginSerializer(user, data=data)
        if serializer.is_valid() :
          return Response(
          {"User" : serializer.data, "Token" : token.key}, status=201)
        else :
          return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    except :
      
      return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
