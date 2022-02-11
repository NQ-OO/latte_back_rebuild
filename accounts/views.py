from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Profile
from .serializers import ProfileSerializer, CreateRandomIdSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response


    
class ProfileAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # Response({"uielements": result})
    def put(self, request, id) :
      if id is None:
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
      else :
        user_profile = Profile.objects.get(id = id)
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
        user_profile = Profile.objects.get(id = id)
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
        return Response(serializer.data, status=201)
      else :
        return Response(serializer.errors, status=400)



      
      return Response(serializer.data, status=status.HTTP_200_OK)