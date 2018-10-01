from django import forms
from .models import Comment #Comment_To_Node, Comment_To_Edge #Node, Edge
from captcha.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = ('text',)