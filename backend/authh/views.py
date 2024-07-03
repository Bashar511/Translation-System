from django.shortcuts import render,redirect
from .forms import  UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.
# 
def welcome(request):
    # Welcome page with user links
    if request.user.is_authenticated :
        return redirect('translation:browse')
    return render(request, 'welcome.html')

def signup(request):
    # Proceed to register the user account
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #to be fixed
            return redirect('translation:browse')  # Redirect to browse_projects view
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def edit(request):
    # Proceed to modify the user account
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile has been updated successfully.')
        else:
            messages.error(request, 'Error updaing your profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def logout_user (request):
    logout(request)
    return render(request, 'registration/logged_out.html')






