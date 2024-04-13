from django import forms
from .models import Fundo

class FundoForm(forms.ModelForm):
    class Meta:
        model = Fundo
        fields = ['fundo', 'idsede']
        widgets = {
            'fundo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idsede': forms.Select(attrs={'class': 'form-control mb-2'}),
        }
