from .models import *
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_time', 'end_time')


class MembersProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MembersProfile
        fields = "__all__"