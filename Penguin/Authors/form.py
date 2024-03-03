from django import forms
from .models import AutherModel

class AuthorForm(forms.ModelForm):
    class Meta:
        model=AutherModel
        fields='__all__'

