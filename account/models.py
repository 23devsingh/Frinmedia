from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='users/Default.jpg')
    bio = models.TextField(max_length=500, blank=True)
    followers = models.ManyToManyField(User, related_name="followers_of_profiles", blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
