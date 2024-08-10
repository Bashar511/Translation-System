from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Specify the input fields to register a new user
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'id': 'password',        })
    )
    password2 = forms.CharField(
        label='Confirm password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'id': 'password2',
        })
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets={
            
            'email': forms.EmailInput(attrs={
            'id':'email',
            'class': 'form-input',
            
            }),
            'username':forms.TextInput(attrs={
            'id':'username',
            'class': 'form-input',
            
            }),
            'first_name':forms.TextInput(attrs={
            'id':'firstname',
            'class': 'form-input',
            
            }),
            # 'password':forms.PasswordInput(attrs={
            # 'id':'confirm-password',
            # 'class': 'form-input',
            
            # }),
            # 'password2':forms.PasswordInput(attrs={
            # 'id':'confirm-password',
            # 'class': 'form-input',
            
            # }),
            
        }
        
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['first_name'].label = "First Name"
        self.fields['email'].label = "Email"
    
    
    
    # to verify the password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
    # to make sure it is correct email
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exists.')
        return data
# Specify the input fields to Edit Profile
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']
        
#     # to make sure it is correct email
#     def clean_email(self):
#         data = self.cleaned_data['email']
#         qs = User.objects.exclude(id=self.instance.id).filter(email=data)
#         if qs.exists():
#             raise forms.ValidationError('Email already exists.')
#         return data
# # Specify the input fields to profile
# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['date_of_birth', 'photo']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already exists.')
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'photo': 'Upload your profile picture',
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        # Adding custom class to the label of the 'photo' field
        self.fields['photo'].label = 'Upload your profile picture'
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['photo'].widget.attrs.update({'label_class': 'custom-label-class'})
