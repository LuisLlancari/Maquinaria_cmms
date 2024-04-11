# importamos django forms
from django import forms
# importamos los modelos
from . models import Sistema

class SistemaForms(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['sistema']
        widgets = {
            'sistema': forms.TextInput(attrs={'class': 'form-control'}),
        }