from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import Profile
from myposts.models import PostImage
from django.contrib.auth.models import User

# Create your views here.

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    images = PostImage.objects.filter(user=user)
    return render(request, 'user_profile/profile.html', {'profile': profile, 'images': images,})
