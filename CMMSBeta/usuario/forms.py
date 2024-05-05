from django import forms
from .models import Rol, Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields  = ['nombres', 'apellidos', 'dni']
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control mb-3', 'id':'txtNombres'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control mb-3', 'id':'txtApellidos'}),
            'dni': forms.TextInput(attrs={'class':'form-control mb-3', 'id':'txtDni'}),
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['idrol', 'rol']
        widgets = {
            'idrol': forms.HiddenInput(),
            'rol': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
