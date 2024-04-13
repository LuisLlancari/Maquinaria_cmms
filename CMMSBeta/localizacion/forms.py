from django import forms
from .models import Sede, Base, Area


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['idsede', 'sede', 'estado']
        widgets = {
            'idsede': forms.HiddenInput(),
            'sede': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BaseForm(forms.ModelForm):
    idsede_id = forms.ModelChoiceField(queryset=Sede.objects.all(
    ), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Base
        fields = ['idbase', 'base', 'estado', 'idsede_id']
        widgets = {
            'idbase': forms.HiddenInput(attrs={'id': 'idbase', 'name': 'idbase'}),
            'base': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AreaForm(forms.ModelForm):
    Base = forms.ModelChoiceField(queryset=Base.objects.all(
    ), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Area
        fields = ['idarea', 'area', 'estado']
        widgets = {
            'idarea': forms.HiddenInput(attrs={'id': 'idarea', 'name': 'idarea'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
