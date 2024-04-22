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
            'idtiposolicitante': forms.Select(attrs={'class': 'form-select', 'id': 'txtSolicitante'}),
            'idpersona': forms.TextInput(attrs={'class': 'form-control', 'id': 'txtApellidos'}),
        }
