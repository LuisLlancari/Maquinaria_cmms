from django import forms
from . models import TipoSolicitante, Tractorista, Solicitante

class TiposolicitanteForms(forms.ModelForm):
    class Meta:
        model = TipoSolicitante
        fields = ['tiposolicitante']
        widgets = {
            'tiposolicitante': forms.TextInput(attrs={'class': 'form-control', 'id':'txtTipoSolicitante'}),
        }

class TractoristaForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TractoristaForms, self).__init__(*args, **kwargs)
        self.fields['idtractorista'].queryset = Tractorista.objects.filter(estado_actividad = True)
    class Meta:
        model = Tractorista
        fields = ['idtractorista','apellidos', 'nombres', 'codigo', 'dni']
        widgets = {
            'idtractorista': forms.HiddenInput(),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id':'txtApellidos'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'id':'txtNombres'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id':'txtCodigo'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'id':'txtDni'}),
        }
        
class SolicitanteForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SolicitanteForms, self).__init__(*args, **kwargs)
        self.fields['idtiposolicitante'].queryset = TipoSolicitante.objects.filter(estado = True)
        
    class Meta:
        model = Solicitante
        fields = ['idsolicitante','idtiposolicitante', 'apellidos', 'nombres', 'codigo']
        widgets = {
            'idsolicitante': forms.HiddenInput(),
            'idtiposolicitante': forms.Select(attrs={'class': 'form-select', 'id': 'txtSolicitante'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtApellidos'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtNombres'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtCodigo'}),
        }
