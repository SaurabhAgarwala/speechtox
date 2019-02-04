from django import forms
from . import models

class InputForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = ['body']
