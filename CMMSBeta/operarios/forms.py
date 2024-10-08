from django import forms
from . models import TipoSolicitante, Tractorista, Solicitante
from usuario.models import Usuario

class TiposolicitanteForms(forms.ModelForm):
    class Meta:
        model = TipoSolicitante
        fields = ['tiposolicitante']
        widgets = {
            'tiposolicitante': forms.TextInput(attrs={'class': 'form-control mt-3', 'id':'txtTipoSolicitante'}),
        }

class TractoristaForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TractoristaForms, self).__init__(*args, **kwargs)
        self.fields['idusuario'].queryset = Usuario.objects.filter(idrol = 2)
        
    class Meta:
        model = Tractorista
        fields = ['idusuario','idpersona']
        widgets = {
            # 'idtractorista': forms.HiddenInput(),
            'idusuario': forms.TextInput(attrs={'class': 'form-control', 'id':'txtApellidos'}),
            'idpersona': forms.TextInput(attrs={'class': 'form-control', 'id':'txtApellidos'}),
        }
        
class SolicitanteForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SolicitanteForms, self).__init__(*args, **kwargs)
        self.fields['idtiposolicitante'].queryset = TipoSolicitante.objects.filter(estado = True)
        
    class Meta:
        model = Solicitante
        fields = ['idtiposolicitante', 'idpersona']
        widgets = {
            'idtiposolicitante': forms.Select(attrs={'class': 'form-select', 'id': 'txtSolicitante', 'required': 'true'}),
            'idpersona': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtApellidos'}),
        }
