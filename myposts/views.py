from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostImageForm
from .models import PostImage


def post_image_view(request):
    if request.method == 'POST':
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            post_image = form.save(commit=False)
            post_image.user = request.user  # Associate the logged-in user
            post_image.save()
            return redirect('user_profile:profile', username=request.user.username)  # Redirect to a page after successful upload
    else:
        form = PostImageForm()
    return render(request, 'myposts/post_image_form.html', {'form': form})

def post_upload_success(request):
    return render(request, 'myposts/post_success.html')
