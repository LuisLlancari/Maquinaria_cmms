from django import forms
from .models import Sede, Base, Area


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['idsede', 'sede']
        widgets = {
            'idsede': forms.HiddenInput(),
            'sede': forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}),
        }


class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = ['idbase', 'base', 'idsede']
        widgets = {
            'idbase': forms.HiddenInput(),
            'base': forms.TextInput(attrs={'class': 'form-control'}),

        }


class AreaForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las opciones del campo idtipotractor
        self.fields['idbase'].queryset = Base.objects.filter(
            estado=True)
    class Meta:
        model = Area
        fields = ['idarea', 'area', 'idbase']
        widgets = {
            'idarea': forms.HiddenInput(attrs={'id': 'idarea', 'name': 'idarea'}),
            'area': forms.TextInput(attrs={'class': 'form-control' }),
            'idbase': forms.Select(attrs={'class': 'form-control mb-2'}),
        }
