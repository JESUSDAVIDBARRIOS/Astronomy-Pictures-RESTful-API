from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from filters.mixins import FiltersMixin

from .serializers import *
from .models import *

class PaginationConfig(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 25

class AstronomyPictureView(FiltersMixin, viewsets.ModelViewSet):
    queryset = AstronomyPicture.objects.all()
    serializer_class = AstronomyPictureSerializer
    pagination_class = PaginationConfig
    
    filter_mappings = {
        'title': 'title__icontains',
        'explanation': 'explanation__icontains'
    }
    
