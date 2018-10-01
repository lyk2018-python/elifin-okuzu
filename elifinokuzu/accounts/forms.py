from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email= self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    # def save(self, commit=True):
    #     user = super(UserLoginForm, self).save(commit=False)
    #     user.username = self.cleaned_data["username"]
    #     user.password = self.cleaned_data["password"]
    #     if commit:
    #         user.authenticate(username=user.username, password=user.password)
    #     return user
