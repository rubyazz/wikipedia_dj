from .models import Word
from django.forms import ModelForm, TextInput


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['name']
        widgets = {'name' :TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a word ...'
        })}