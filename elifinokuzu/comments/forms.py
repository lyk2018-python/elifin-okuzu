from django import forms
from .models import Comment #Node, Edge
from captcha.fields import ReCaptchaField

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = ('text',)
