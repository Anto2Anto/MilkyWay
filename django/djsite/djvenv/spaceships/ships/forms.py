from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class RegisterUserForm(UserCreationForm):
        #def __init__(self):
                #super(UserCreationForm, self).__init__()

        username = forms.CharField(label = 'Log in', widget = forms.TextInput(attrs = {'class': 'form-input'}))
        email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs = {'class': 'form-input'}))
        password1 = forms.CharField(label = 'Password', widget = forms.TextInput(attrs = {'class': 'form-input'}))
        password2 = forms.CharField(label = 'Confirm Password',
                                    widget = forms.PasswordInput(attrs = {'class': 'form-input'}))

        class Meta:
                model = User
                fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
        username = forms.CharField(label = 'Log in', widget = forms.TextInput(attrs = {'class': 'form-input'}))
        password = forms.CharField(label = 'Password', widget = forms.TextInput(attrs = {'class': 'form-input'}))


class Feedback(forms.Form):
        name = forms.CharField(label = 'Name')
        email = forms.EmailField(label = 'Email')
        content = forms.CharField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 10}))
        captcha = CaptchaField()