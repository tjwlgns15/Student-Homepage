from django import forms
from .models import Free_Board

class Free_BoardForm(forms.ModelForm):
    class Meta:
        model = Free_Board
        fields = ['title', 'content']