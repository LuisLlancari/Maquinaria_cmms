from django import forms
from .models import TipoTractor, Tractor
from .models import ReporteTractor

class TipoTractorForm(forms.ModelForm):
    class Meta:
        model = TipoTractor
        fields = ['idtipotractor', 'TipoTractor']
        widgets = {
            'idtipotractor': forms.HiddenInput(),
            'TipoTractor': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class TractorForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las opciones del campo idtipotractor
        self.fields['idtipotractor'].queryset = TipoTractor.objects.filter(estado=True)
        self.fields['idtractor'].queryset = Tractor.objects.filter(estado_actividad=True)
    class Meta:
        model = Tractor
        fields = ['idtractor','idtipotractor', 'idusuario', 'nrotractor', 'horainicial', 'horauso']
        widgets = {
            'idtractor': forms.HiddenInput(),  # Campo oculto
            'idtipotractor': forms.Select(attrs={'class': 'form-control'}),
            'idusuario': forms.Select(attrs={'class': 'form-control'}),
            'nrotractor': forms.TextInput(attrs={'class': 'form-control'}),
            'horainicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horauso': forms.NumberInput(attrs={'class': 'form-control'}),
        }




class ReporteTractorForm(forms.ModelForm):
    class Meta:
        model = ReporteTractor
        fields = ['idusuario', 'idprogramacion','horometroinicial', 'horometrofinal', 'correlativo']
        widgets = {
            'idusuario': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}),
            'idprogramacion': forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
            'horometroinicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horometrofinal': forms.NumberInput(attrs={'class': 'form-control'}),
            'correlativo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

