from django.contrib import admin
from .models import PostImage

# Register your models here.
@admin.register(PostImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'image', 'description', 'created']
    list_filter = ['created']