from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Profile
from .serializers import ProfileSerializer
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
        
    