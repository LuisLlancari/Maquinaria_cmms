from django import forms
from .models import TipoTractor

class TipoTractorForm(forms.ModelForm):
    class Meta:
        model = TipoTractor
        fields = ['TipoTractor', 'estado']
        widgets = {
            'TipoTractor': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

