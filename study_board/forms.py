from django import forms
from .models import Study_Board

class Study_BoardForm(forms.ModelForm):
    class Meta:
        model = Study_Board
        fields = ['title', 'content']