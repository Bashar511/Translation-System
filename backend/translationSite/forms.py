from django import forms
from .models import *
from django.contrib.auth.models import User

# Specify the input fields to new project
class projectForm(forms.ModelForm):
        class Meta:
            model = Project
            fields = ['title', 'publish','deliverytime','fileEN']

class PermissionForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['project', 'granted_to']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PermissionForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(owner=user)