from rest_framework import serializers
# from whatthegam.models import School
from .models import Profile

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Profile 
    fields = '__all__'


