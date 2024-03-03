from django import forms
from .models import PublisherModel

class PublisherForm(forms.ModelForm):
    class Meta:
        model=PublisherModel
        fields='__all__'