from django import forms
from .models import Sede, Base, Area


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['idsede', 'sede']
        widgets = {
            'idsede': forms.HiddenInput(),
            'sede': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = ['idbase', 'base', 'idsede']
        widgets = {
            'idbase': forms.HiddenInput(),
            'base': forms.TextInput(attrs={'class': 'form-control'}),
            'idsede': forms.Select(attrs={'class': 'form-control mb-2'}),
        }

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['idarea', 'area', 'idbase']
        widgets = {
            'idarea': forms.HiddenInput(attrs={'id': 'idarea', 'name': 'idarea'}),
            'area': forms.TextInput(attrs={'class': 'form-control' }),
            'idbase': forms.Select(attrs={'class': 'form-control mb-2'}),
        }
