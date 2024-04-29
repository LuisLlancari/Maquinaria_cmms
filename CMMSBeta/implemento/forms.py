from django import forms
from . models import Implemento, DetImplementos, TipoImplemento
from usuario.models import Usuario


class ImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(ImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idtipoimplemento'].queryset = TipoImplemento.objects.filter(estado = True)
        self.fields['idusuario'].queryset = Usuario.objects.filter(idrol = 2)
  class Meta:
    model = Implemento
    fields = ['idimplemento','idusuario','implemento','tiempovida','horasdeuso', 'codimplemento', 'idtipoimplemento', 'idceco','idarea']
    widgets = {
      'idimplemento': forms.HiddenInput(),
      'implemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtImplemento'}),
      'idusuario': forms.Select(attrs={'class':'form-select', 'id':'txtIdUsuario'}),
      'tiempovida': forms.TextInput(attrs={'class':'form-control', 'id':'txtTiempoVida'}),
      'horasdeuso': forms.TextInput(attrs={'class':'form-control', 'id':'txtHorasUso'}),
      'codimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtCodImplemento'}),
      'idtipoimplemento': forms.Select(attrs={'class':'form-control', 'id':'txtIdTipoimplemento'}),
      'idceco': forms.Select(attrs={'class':'form-control', 'id':'txtIdCeco'}),
      'idarea': forms.Select(attrs={'class':'form-control', 'id':'txtIdArea'}) 
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
    fields = ['tipoimplemento']
    widgets = {
      'tipoimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtTipoImplemento'})
    }