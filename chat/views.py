from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import Profile
from myposts.models import PostImage

# Create your views here.

@login_required
def message_view(request):
    return render(request,
                'chat/messages.html')