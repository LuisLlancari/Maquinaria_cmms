from django import forms
from .models import Rol, Persona, Usuario
from django.contrib.auth.forms import UserCreationForm


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

class UsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        
    class Meta:
        model = Usuario
        fields = {'username', 'first_name', 'last_name', 'password1', 'password2', 'idrol'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'idrol': forms.Select(attrs={'class':'form-select bm-3'}),
            'first_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control mb-3'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control bm-3'}),
        }

  