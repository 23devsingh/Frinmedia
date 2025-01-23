from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
from myposts.models import PostImage
from django.contrib.postgres.search import SearchVector

# Create your views here.

#@login_required
#def search(request):
#    return render(request,
#                'search/search.html')


@login_required
def search_users(request):
    query = request.GET.get('q')
    users = User.objects.none()
    profile = Profile.objects.get(user=request.user)
    if query:
        users = User.objects.filter(username__icontains=query)

    return render(request, 'search/search.html', {'users': users, 'query': query, 'profile': profile})
