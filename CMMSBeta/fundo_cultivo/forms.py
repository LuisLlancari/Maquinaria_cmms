from django import forms
from .models import Fundo, Cultivo

class FundoForm(forms.ModelForm):
    class Meta:
        model = Fundo
        fields = ['fundo', 'idsede']
        widgets = {
            'fundo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idsede': forms.Select(attrs={'class': 'form-control mb-2'}),
        }

class CultivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CultivoForm, self).__init__(*args, **kwargs)
        self.fields['idfundo'].queryset = Fundo.objects.filter(estado=True)

    class Meta:
        model = Cultivo
        fields = ['cultivo', 'idfundo']
        widgets = {
            'cultivo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idfundo': forms.Select(attrs={'class': 'form-control mb-2'}),
        }
