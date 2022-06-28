from django import forms
from .models import Note


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("picture",)
