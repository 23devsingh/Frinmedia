from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm , ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from myposts.models import PostImage

# Create your views here.

def user_login(request):

    #capture the next url if provided in the query sting
    next_url = request.GET.get('next')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username_or_email=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return redirect(next_url if next_url else 'home')
                    return redirect(reverse('account:home'))
                else:
                    #return HttpResponse('Disabled account')
                    form.add_error(None, 'Disabled account')

            else:
                #return HttpResponse('Invalid Login')
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'account/login2.html', {'form': form, 'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('account:login')



@login_required
def home(request):
    images = PostImage.objects.filter(privacy='public').select_related('user')
    profile = Profile.objects.select_related('user', 'user_profile').all()
    return render(request,
                'account/home.html',
                {'section': 'home', 'images': images, 'profile': profile})


#For Signup the User
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            #Save the User object
            new_user.save()
            #create the user profile
            Profile.objects.create(user=new_user)

            return render(request, 'account/signup_done.html', {'new_user' : new_user})
        else:
            # Add error messages for the user to see
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/signup.html', {'user_form': user_form})



@login_required
def edit(request):
    if request.method == 'POST':
        user_form =  UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('user_profile:profile', username=request.user.username)

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,
                'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def edit_done(request):
    return render(request,'account/edit_done.html')