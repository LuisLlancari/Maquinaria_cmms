from django import forms
from . models import Implemento, DetImplementos, TipoImplemento


class ImplementoForms(forms.ModelForm):
  class Meta:
    model = Implemento
    fields = ['implemento','tiempovida', 'nroimplemento', 'codimplemento', 'idtipoimplemento', 'idarea']
    widgets = {
      'implemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtImplemento'}),
      'tiempovida': forms.TextInput(attrs={'class':'form-control', 'id':'txtTiempoVida'}),
      'nroimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtNroImplemento'}),
      'codimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtCodImplemento'}),
      'idtipoimplemento': forms.Select(attrs={'class':'form-control', 'id':'txtIdTipoimplemento'}),
      'idarea': forms.Select(attrs={'class':'form-control', 'id':'txtIdArea'}) 
    }

    
class DetImplementoForms(forms.ModelForm):
  class Meta:
    model = DetImplementos
    fields = ['idresponsable','idpieza', 'idceco', 'idimplemento']
    widgets = {
      'idresponsable': forms.TextInput(attrs={'class':'form-control', 'id':'txtIdResponsable'}),
      'idpieza': forms.TextInput(attrs={'class':'form-control', 'id':'txtIdpieza'}),
      'idceco': forms.TextInput(attrs={'class':'form-control', 'id':'txtIdCeco'}),
      'idimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtIdImplemento'}),
    }

class TipoImplementoForms(forms.ModelForm):
  class Meta:
    model = TipoImplemento
    fields = ['tipoimplemento']
    widgets = {
      'tipoimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtTipoImplemento'})
    }