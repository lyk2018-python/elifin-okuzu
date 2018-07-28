from django import forms
from .models import LANGUAGE_CHOICES, EDGE_TYPE_CHOICES


class SubmissionForm(forms.Form):
    source_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label='Source Language',
    )
    source_node = forms.CharField(
        help_text="Example: Elif in Turkish language",
        max_length=255,
        label='Source Node',
    )
    target_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label='Target Language',
    )
    target_node = forms.CharField(
        help_text="Example: Alpha in Ancient Greek",
        max_length=255,
        label='Target Node',
    )
    type_of_edge = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=EDGE_TYPE_CHOICES,
        label='Type of Edge',
    )
    resource = forms.CharField(
        help_text="Example: Sevan Nişanyan's Elifin Öküzü",
        max_length=255,
        label='Resource',
    )

class Search(forms.Form):
    search=forms.CharField(
        max_length=255,
        )

