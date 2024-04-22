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
        fields = ['idtractorista','idusuario','idpersona']
        widgets = {
            'idtractorista': forms.HiddenInput(),
            'idusuario': forms.Select(attrs={'class': 'form-select', 'id':'txtTractorista'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id':'txtPersona'}),
        }
        
class SolicitanteForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SolicitanteForms, self).__init__(*args, **kwargs)
        self.fields['idtiposolicitante'].queryset = TipoSolicitante.objects.filter(estado = True)
        
    class Meta:
        model = Solicitante
        fields = ['idsolicitante','idtiposolicitante','idpersona']
        widgets = {
            'idsolicitante': forms.HiddenInput(),
            'idtiposolicitante': forms.Select(attrs={'class': 'form-select', 'id': 'txtSolicitante'}),
            'idpersona' : forms.Select(attrs={'class': 'form-select', 'id': 'txtPersona'}),
        }
