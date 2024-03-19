from django import forms
from .models import *
from django.contrib.auth.models import User

# Specify the input fields to new project
class projectForm(forms.ModelForm):
        class Meta:
            model = project1
            fields = ['title', 'publish','deliverytime','fileEN']
            
            
            