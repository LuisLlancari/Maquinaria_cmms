from django import forms
from .models import *
from tractor.models import *
from operarios.models import *

class TipoLaborForm(forms.ModelForm):
    class Meta:
        model = TipoLabor
        fields = ['tipolabor']
        widgets = {
            'tipolabor': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }

class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ['idtipolabor', 'idlote', 'idtractor', 'idusuario', 'idtractorista', 'idsolicitante', 'fechahora', 'turno']
        widgets = {
            'idtipolabor': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idlote': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idtractor': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idusuario': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idtractorista': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idsolicitante': forms.Select(attrs={'class': 'form-control mb-2'}),
            'fechahora': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'turno': forms.Select(attrs={'class': 'form-control mb-2'}),
        }
        

class DetalleLaborForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idimplemento'].queryset = Implemento.objects.filter(estado_actividad = True, estado = True)
    class Meta:
        model = DetalleLabor
        fields = ['idimplemento', 'idprogramacion', 'horadeuso']
        widgets = {
            'idimplemento': forms.Select(attrs={'class': 'form-control mb-2 '}),
            'idprogramacion': forms.Select(attrs={'class': 'form-control mb-2 '}),
            'horadeuso': forms.TimeInput(attrs={'class': 'form-control mb-2 '}),
        }