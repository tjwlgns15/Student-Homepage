from django import forms
from .models import study

class studyForm(forms.ModelForm):
    class Meta:
        model = study
        fields = ['title', 'content', 'people']