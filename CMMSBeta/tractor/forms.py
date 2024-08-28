from django import forms
from .models import TipoTractor, Tractor, TractorSupervisor
from .models import ReporteTractor
from usuario.models import Usuario
from django.utils import timezone
from fundo_cultivo.models import Fundo

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
        self.fields['idfundo'].queryset = Fundo.objects.filter(estado=True)
    class Meta:
        model = Tractor
        fields = ['idtractor','idtipotractor', 'idfundo' ,'nrotractor', 'horainicial', 'horauso']
        widgets = {
            'idtractor': forms.HiddenInput(),  # Campo oculto
            'idtipotractor': forms.Select(attrs={'class': 'form-control'}),
            'idfundo': forms.Select(attrs={'class': 'form-control'}),
            'nrotractor': forms.TextInput(attrs={'class': 'form-control'}),
            'horainicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'horauso': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'readonly': True}),
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

class TractorSupervisorForms(forms.ModelForm):
   def __init__(self, *args, **kwargs):
      super(TractorSupervisorForms, self).__init__(*args, **kwargs)
      self.fields['idsupervisor'].queryset = Usuario.objects.filter(idrol = 3, is_active = 1)

      # obtenemos los id de los tractores que ya estan en la registro
      exclude_tractors = TractorSupervisor.objects.filter(estado=True).values_list('idtractor', flat=True)
      self.fields['idtractor'].queryset = Tractor.objects.filter(estado = True).exclude(idtractor__in=exclude_tractors)



   class Meta:
      ahora = timezone.localtime()
      fecha_actual = ahora.date()

      model = TractorSupervisor
      fields = ['idtractor', 'idsupervisor', 'fechaInicio']
      widgets = {
         'idtractor': forms.Select(attrs={'class':'form-select', 'id':'txtTractor'}),
         'idsupervisor': forms.Select(attrs={'class':'form-select', 'id':'txtSupervisor'}),
         'fechaInicio': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'id':'txtFechainicio', 'min':fecha_actual}),
      }

