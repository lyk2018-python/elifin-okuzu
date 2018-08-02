from django.forms import ModelForm
from .models import SupportText
from captcha.fields import ReCaptchaField

class SupportForm(ModelForm):
    class Meta:
        model = SupportText
        fields = ['title',"problem"]

    captcha = ReCaptchaField()
