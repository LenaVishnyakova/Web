from django import forms
from django.forms import TextInput

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['header', 'note_text']

        widgets = {
            'header': TextInput(),
            'note_text': TextInput()
        }
