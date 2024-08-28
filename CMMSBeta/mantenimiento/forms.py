from django import forms
from .models import Acciones

class AccionesForms(forms.ModelForm):
  
  class Meta:
    model= Acciones
    fields = ['accion', 'estado']
    widgets={
      'accion': forms.TextInput(attrs={'class':'form-control mt-2 mb-2', 'id':'txtAccion'}),
      'estado': forms.Select(attrs={'class':'form-select mt-2 mb-2', 'id':'txtEstado'}),
    }
  