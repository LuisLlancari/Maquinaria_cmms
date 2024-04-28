# importamos django forms
from django import forms
# importamos los modelos
from . models import Sistema, Componente

class SistemaForms(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['sistema']
        widgets = {
            'sistema': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtsistema'}),
        }

class ComponenteForms(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['componente','idsistema' ,'codcomponente', 'tiempovida']
        widgets = {
            'idsistema': forms.Select(attrs={'class':'form-control', 'id': 'txtsistema'}),
            'componente': forms.TextInput(attrs={'class':'form-control', 'id': 'txtComponente'}),
            'codcomponente': forms.TextInput(attrs={'class':'form-control', 'id': 'txtCodigoComp'}),
            'tiempovida': forms.TextInput(attrs={'class':'form-control', 'id': 'txtTiempovida'}),
        }