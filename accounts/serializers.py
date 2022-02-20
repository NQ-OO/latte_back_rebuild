from tkinter.messagebox import NO
from rest_framework import serializers
# from whatthegam.models import School
from .models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.authtoken.models import Token




class ProfileSerializer(serializers.ModelSerializer) :

  class Meta :
    model = Profile 
    fields = '__all__'


class CreateRandomIdSerializer(serializers.ModelSerializer) :
  class Meta :
    model = User
    fields = '__all__'
    
  def create(self, validated_data):
    user = User.objects.create_user( validated_data["username"], validated_data["email"], validated_data["password"])
    return user
  
  
class ChangeUserInfoSerializer(serializers.ModelSerializer) :
  class Meta :
    model = User
    fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    