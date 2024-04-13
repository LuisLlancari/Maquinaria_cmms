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
    class Meta:
        model = Tractorista
        fields = ['apellidos', 'nombres', 'codigo', 'dni']
        widgets = {
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id':'txtApellidos'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'id':'txtNombres'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id':'txtCodigo'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'id':'txtDni'}),
        }
        
class SolicitanteForms(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['idtiposolicitante', 'apellidos', 'nombres', 'codigo']
        widgets = {
            'idtiposolicitante': forms.Select(attrs={'class': 'form-select', 'id': 'txtSolicitante'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtApellidos'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtNombres'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtCodigo'}),
        }
