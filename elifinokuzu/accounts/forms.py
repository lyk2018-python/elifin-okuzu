from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ("username","email")

    def save(self, commit=True):
        # import pdb
        # pdb.set_trace()
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email= self.cleaned_data["email"]
        if commit:
            user.save()
        return user
