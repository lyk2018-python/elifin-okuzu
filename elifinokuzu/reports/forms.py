from django.forms import ModelForm
from .models import Issue

class ReportForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['url',"explantation"]