from django import forms
from . models import Implemento, DetImplementos, TipoImplemento


class ImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(ImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idtipoimplemento'].queryset = TipoImplemento.objects.filter(estado = True)
  class Meta:
    model = Implemento
    fields = ['idimplemento','implemento','tiempovida', 'codimplemento', 'idtipoimplemento', 'idarea']
    widgets = {
      'idimplemento': forms.HiddenInput(),
      'implemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtImplemento'}),
      'tiempovida': forms.TextInput(attrs={'class':'form-control', 'id':'txtTiempoVida'}),
      # 'nroimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtNroImplemento'}),
      'codimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtCodImplemento'}),
      'idtipoimplemento': forms.Select(attrs={'class':'form-control', 'id':'txtIdTipoimplemento'}),
      'idarea': forms.Select(attrs={'class':'form-control', 'id':'txtIdArea'}) 
    }

    
class DetImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(DetImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idimplemento'].queryset = Implemento.objects.filter(estado = True)
  class Meta:
    model = DetImplementos
    fields = ['idresponsable','idpieza', 'idceco', 'idimplemento']
    widgets = {
      'idresponsable': forms.Select(attrs={'class':'form-select', 'id':'txtIdResponsable'}),
      'idpieza': forms.Select(attrs={'class':'form-select', 'id':'txtIdpieza'}),
      'idceco': forms.Select(attrs={'class':'form-select', 'id':'txtIdCeco'}),
      'idimplemento': forms.Select(attrs={'class':'form-select', 'id':'txtIdImplemento'}),
    }

class TipoImplementoForms(forms.ModelForm):
  class Meta:
    model = TipoImplemento
    fields = ['tipoimplemento']
    widgets = {
      'tipoimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtTipoImplemento'})
    }