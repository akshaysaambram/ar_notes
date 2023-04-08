from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'mt-3'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={'placeholder':'Email address'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Confirm your Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
