from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'


urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('edit/', views.edit, name='edit'),
    path('edit_done/', views.edit_done, name='edit_done'),
]
