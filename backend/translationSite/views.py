from django.shortcuts import render
from django.http import HttpResponse
from .api import hel_en2ar, bart_en2ar
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout


def home(request):
    if request.method == 'POST':
        text = request.POST['text_field']
        #processed_text = hel_en2ar(text)
        processed_text = bart_en2ar(text)
        context = {
        'unprocessed' : text,
        'processed' : processed_text,
        }
    else:
        context = {
            'unprocessed' : '',
            'processed' : 'Translated Text',
           
        }
    return render(request, "index.html", context)





@login_required
def index(request):
    return render(request, 'index.html', {'section': 'index'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.name = new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def edit(request):
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
