from django import forms
from .models import Sistema, Componente, Pieza, ConfiguracionTipoImplemento, DetalleComponente

class SistemaForms(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['sistema']
        widgets = {
            'sistema': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtsistema'}),
        }

class ComponenteForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idsistema'].queryset = Sistema.objects.filter(estado=True)
    
    class Meta:
        model = Componente
        fields = ['componente', 'idsistema', 'codcomponente', 'tiempovida', 'frecuencia_man']
        widgets = {
            'idsistema': forms.Select(attrs={'class':'form-control', 'id': 'txtsistema'}),
            'componente': forms.TextInput(attrs={'class':'form-control', 'id': 'txtComponente'}),
            'codcomponente': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtCodigoComp', 'min': 0}),
            'tiempovida': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtTiempovida', 'min': 0}),
            'frecuencia_man': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtFrecuenciaMan', 'min': 0}),
        }

class PiezaForms(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['pieza', 'cantidad_piezas','codpieza', 'frecuencia_man', 'tiempovida']
        widgets = {
            'pieza': forms.TextInput(attrs={'class':'form-control', 'id': 'txtPieza'}),
            'codpieza': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtCodPieza', 'min': 0}),
            'cantidad_piezas': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtCantidadPiezas', 'min': 1}),
            'frecuencia_man': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtFrecuenciaMan', 'min': 0}),
            'tiempovida': forms.NumberInput(attrs={'class':'form-control', 'id': 'txtTiempovida', 'min': 0}),
        }

class DetalleComponenteForms(forms.ModelForm):
    class Meta:
        model = DetalleComponente
        fields = ['idcomponente', 'idpieza', 'cantidad']
        widgets = {
            'idcomponente': forms.Select(attrs={'class': 'form-control', 'id': 'txtComponente'}),
            'idpieza': forms.Select(attrs={'class': 'form-control', 'id': 'txtPieza'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'id': 'txtPieza', 'min': 1}),
        }  

