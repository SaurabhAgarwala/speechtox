from django import forms
from . import models

class NumberOfSongsForm(forms.ModelForm):
    class Meta:
        model = models.NumberOfSongs
        fields = ['number_of_songs']
