from django.urls import path
from . import views

app_name = 'myposts'

urlpatterns = [
    path('upload/', views.post_image_view, name='post_image_upload'),
    path('upload/success/', views.post_upload_success, name='post_success'),
]
