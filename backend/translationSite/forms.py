from django import forms
from .models import *
from django.contrib.auth.models import User

# Specify the input fields to new project
class projectForm(forms.ModelForm):
        class Meta:
            model = Project
            fields = ['title', 'publish','deliverytime','fileEN']
            widgets={
            
            'title': forms.TextInput(attrs={
            'id':'Title',
            'class': 'form-create',
            
            }),
            'publish':forms.TextInput(attrs={
            'id':'publish',
            'class': 'form-create',
            
            }),
            'deliverytime':forms.TextInput(attrs={
            'id':'deliverytime',
            'class': 'form-create',
            
            }),
            'fileEN': forms.FileInput(attrs={
            'id':'fileEN',
            'class': 'form-create'}),}
            labels = {'fileEN': 'File',}
    
        def __init__(self, *args, **kwargs):
            super(projectForm, self).__init__(*args, **kwargs)
            # Adding custom class to the label of the 'photo' field
            self.fields['fileEN'].label = 'File'
            self.fields['fileEN'].widget.attrs.update({'class': 'form-control-file'})
            self.fields['fileEN'].widget.attrs.update({'label_class': 'custom-label-class'})





















class PermissionForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['project', 'granted_to']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PermissionForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(owner=user)