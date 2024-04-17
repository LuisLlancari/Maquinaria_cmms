from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['idrol', 'rol']
        widgets = {
            'idrol': forms.HiddenInput(),
            'rol': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }
