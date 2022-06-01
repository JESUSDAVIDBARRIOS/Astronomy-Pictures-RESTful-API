from dataclasses import fields
from rest_framework import serializers
from .models import *

class AstronomyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyPicture
        fields = '__all__'
