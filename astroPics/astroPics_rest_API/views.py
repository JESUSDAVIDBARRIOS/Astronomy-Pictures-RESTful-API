from django.shortcuts import render

from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from .models import *

class AstronomyPictureView(viewsets.ModelViewSet):
    queryset = AstronomyPicture.objects.all()
    serializer_class = AstronomyPictureSerializer
