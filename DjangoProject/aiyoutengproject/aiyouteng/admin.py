from django.contrib import admin
from .models import Platform, VideoCategory, SeriesCategory, MoviesCategory, VerietyCategory, Video
# Register your models here.

admin.site.register(Platform)
admin.site.register(VideoCategory)
admin.site.register(SeriesCategory)
admin.site.register(MoviesCategory)
admin.site.register(VerietyCategory)
admin.site.register(Video)