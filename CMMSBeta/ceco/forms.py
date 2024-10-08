from django import forms
from .models import *

class CecoForm(forms.ModelForm):
    class Meta:
        model = Ceco
        fields = ['ceco']
        widgets = {
            'ceco': forms.TextInput(attrs={'class': 'form-control mb-2', 'required':'true'}),
        }