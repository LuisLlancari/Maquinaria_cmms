# importamos django forms
from django import forms
# importamos los modelos
from . models import Sistema, Pieza, Componente

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
        fields = ['componente', 'codcomponente', 'horainstalacion', 'tiempovida', 'idsistema']
        widgets = {
            'componente': forms.TextInput(attrs={'class':'form-control', 'id': 'txtComponente'}),
            'codcomponente': forms.TextInput(attrs={'class':'form-control', 'id': 'txtCodigoComp'}),
            'horainstalacion': forms.TextInput(attrs={'class':'form-control', 'id': 'txthoraInstalacion'}),
            'tiempovida': forms.TextInput(attrs={'class':'form-control', 'id': 'txtTiempovida'}),
            'idsistema': forms.Select(attrs={'class':'form-select', 'id': 'txtSistema'}),
        }
class PiezaForms(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['pieza', 'codpieza', 'tiempoinstalacion', 'tiempovida', 'frecuenciaMP', 'idcomponente']
        widgets = {
            'pieza': forms.TextInput(attrs={'class': 'form-control', 'id':'txtPieza'}),
            'codpieza': forms.TextInput(attrs={'class': 'form-control', 'id':'txtCodPieza'}),
            'tiempoinstalacion': forms.TextInput(attrs={'class':'form-control','id':'txtTiempoInslacion'}),
            'tiempovida': forms.TextInput(attrs={'class': 'form-control', 'id':'txtTiempoVida'}),
            'frecuenciaMP': forms.TextInput(attrs={'class': 'form-control', 'id':'txtFrecuenciaMP'}),
            'idcomponente': forms.Select(attrs={'class': 'form-select', 'id':'txtComponente'}),

        }