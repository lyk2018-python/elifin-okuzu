from django.forms import ModelForm
from .models import Issue
from captcha.fields import ReCaptchaField
class ReportForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title',"explantation"]

    captcha = ReCaptchaField()
