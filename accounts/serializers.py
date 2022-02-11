from rest_framework import serializers
# from whatthegam.models import School
from .models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer) :

  class Meta :
    model = Profile 
    fields = '__all__'


class CreateRandomIdSerializer(serializers.ModelSerializer) :
  class Meta :
    model = User
    fields = '__all__'