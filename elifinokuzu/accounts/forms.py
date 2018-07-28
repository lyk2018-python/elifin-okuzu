from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
