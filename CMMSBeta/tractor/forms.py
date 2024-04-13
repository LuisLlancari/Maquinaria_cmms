from django import forms
from .models import TipoTractor, Tractor

class TipoTractorForm(forms.ModelForm):
    class Meta:
        model = TipoTractor
        fields = ['TipoTractor', 'estado']
        widgets = {
            'TipoTractor': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractor
        fields = '__all__'
        widgets = {
            'idtipotractor': forms.Select(attrs={'class': 'form-control'}),
            'idusuario': forms.Select(attrs={'class': 'form-control'}),
            'nrotractor': forms.TextInput(attrs={'class': 'form-control'}),
            'horainicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horauso': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idtractor': forms.HiddenInput(),  # Campo oculto
        }

from django import forms
from .models import ReporteTractor

class ReporteTractorForm(forms.ModelForm):
    class Meta:
        model = ReporteTractor
        fields = ['idusuario', 'horometroinicial', 'horometrofinal', 'correlativo', 'estado']
        labels = {
            'idusuario': 'Usuario',
            'horometroinicial': 'Horómetro Inicial',
            'horometrofinal': 'Horómetro Final',
            'correlativo': 'Correlativo',
            'estado': 'Estado',
        }
        widgets = {
            'idusuario': forms.Select(attrs={'class': 'form-control'}),
            'horometroinicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horometrofinal': forms.NumberInput(attrs={'class': 'form-control'}),
            'correlativo': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

