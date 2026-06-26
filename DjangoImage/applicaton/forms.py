from django import forms
from .models import imageModel

class imageForms(forms.ModelForm):
    class Meta:
        model=imageModel
        fields=["imageName","image"]