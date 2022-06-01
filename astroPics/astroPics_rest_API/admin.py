from django.contrib import admin
from .models import *

class AstronomyPictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# Register your models here.
admin.site.register(AstronomyPicture)

