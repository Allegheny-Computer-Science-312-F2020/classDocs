from django.contrib import admin
from .models import Album, Song
# from music/models.py class
##
admin.site.register(Album)
admin.site.register(Song)
