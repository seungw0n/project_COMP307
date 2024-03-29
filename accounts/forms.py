from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    address = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', )
        
class EditProfileForm(ModelForm):
    address = forms.CharField(max_length=500)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']