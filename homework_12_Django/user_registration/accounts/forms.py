from django import forms

from .models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)


class UserLogin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
