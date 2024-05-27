from django import forms
from . models import Implemento, DetImplementos, TipoImplemento
from usuario.models import Usuario

from ceco.models import Ceco
from localizacion.models import Area

class ImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(ImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idtipoimplemento'].queryset = TipoImplemento.objects.filter(estado = True)
        self.fields['idusuario'].queryset = Usuario.objects.filter(idrol = 3)
        self.fields['idceco'].queryset = Ceco.objects.filter(estado = True)
  class Meta:
    model = Implemento
    fields = ['idimplemento','idusuario','implemento','horasdeuso', 'codimplemento', 'idtipoimplemento', 'idceco']
    widgets = {
      'idimplemento': forms.HiddenInput(),
      'implemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtImplemento'}),
      'idusuario': forms.Select(attrs={'class':'form-select', 'id':'txtIdUsuario'}),
      'horasdeuso': forms.NumberInput(attrs={'class':'form-control', 'id':'txtHorasUso', 'type':'number', 'min':'0'}),
      'codimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtCodImplemento'}),
      'idtipoimplemento': forms.Select(attrs={'class':'form-control', 'id':'txtIdTipoimplemento'}),
      'idceco': forms.Select(attrs={'class':'form-control', 'id':'txtIdCeco'}),
    }

    
class DetImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(DetImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idimplemento'].queryset = Implemento.objects.filter(estado = True)
  class Meta:
    model = DetImplementos
    fields = ['idimplemento']
    widgets = {
      'idimplemento': forms.Select(attrs={'class':'form-select', 'id':'txtIdImplemento'}),
    }

class TipoImplementoForms(forms.ModelForm):
  class Meta:
    model = TipoImplemento
    fields = ['tipoimplemento', 'idconfiguracion_implemento']
    widgets = {
      'tipoimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtTipoImplemento'}),
      'idconfiguracion_implemento': forms.Select(attrs={'class':'form-select', 'id':'txtIdConfiguracionImplemento'}),
    }