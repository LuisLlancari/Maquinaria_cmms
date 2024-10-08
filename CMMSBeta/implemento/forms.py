from django import forms
from . models import Implemento, DetImplementos, TipoImplemento, ImplementoSupervisor
from usuario.models import Usuario
from ceco.models import Ceco
from django.utils import timezone


class ImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(ImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idtipoimplemento'].queryset = TipoImplemento.objects.filter(estado = True)
        # self.fields['idusuario'].queryset = Usuario.objects.filter(idrol = 3, is_active = 1)
        self.fields['idceco'].queryset = Ceco.objects.filter(estado = True)
  class Meta:
    model = Implemento
    fields = ['idimplemento','implemento','horasdeuso', 'codimplemento', 'idtipoimplemento', 'idceco']
    widgets = {
      'idimplemento': forms.HiddenInput(),
      'implemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtImplemento'}),
      # 'idusuario': forms.Select(attrs={'class':'form-select', 'id':'txtIdUsuario'}),
      'horasdeuso': forms.NumberInput(attrs={'class':'form-control', 'id':'txtHorasUso', 'type':'number', 'min':'0', 'readonly':'readonly'}),
      'codimplemento': forms.TextInput(attrs={'class':'form-control', 'id':'txtCodImplemento'}),
      'idtipoimplemento': forms.Select(attrs={'class':'form-control', 'id':'txtIdTipoimplemento'}),
      'idceco': forms.Select(attrs={'class':'form-control', 'id':'txtIdCeco'}),
    }

    
class DetImplementoForms(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(DetImplementoForms, self).__init__(*args, **kwargs)
        self.fields['idimplemento'].queryset = Implemento.objects.filter(estado = True)
  class Meta:
    model = DetImplementos
    fields = ['idimplemento']
    widgets = {
      'idimplemento': forms.Select(attrs={'class':'form-select', 'id':'txtIdImplemento'}),
    }

class TipoImplementoForms(forms.ModelForm):
  class Meta:
    model = TipoImplemento
    fields = ['tipoimplemento', 'idconfiguracion_implemento', 'tiempo_vida', 'frecuencia_man']
    widgets = {
      'tipoimplemento': forms.TextInput(attrs={'class':'form-control mb-2', 'id':'txtTipoImplemento'}),
      'idconfiguracion_implemento': forms.Select(attrs={'class':'form-select mb-2', 'id':'txtIdConfiguracionImplemento'}),
      'tiempo_vida': forms.NumberInput(attrs={'class':'form-control mb-2', 'id':'txtTiempoVida', 'type':'number', 'min':'0'}),
      'frecuencia_man': forms.NumberInput(attrs={'class':'form-control mb-2', 'id':'txtFrecuenciaMan', 'type':'number', 'min':'0'}),
    }
  
class ImplementoSupervisorForms(forms.ModelForm):
   def __init__(self, *args, **kwargs):
      super(ImplementoSupervisorForms, self).__init__(*args, **kwargs)
      self.fields['idsupervisor'].queryset = Usuario.objects.filter(idrol = 3, is_active = 1)

      # obtenemos los id de los tractores que ya estan en la registro
      excluir_implementos = ImplementoSupervisor.objects.filter(estado=True).values_list('idimplemento', flat=True)
      self.fields['idimplemento'].queryset = Implemento.objects.filter(estado = True).exclude(idimplemento__in=excluir_implementos)


   class Meta:
      ahora = timezone.localtime()
      fecha_actual = ahora.date()

      model = ImplementoSupervisor
      fields = ['idimplemento', 'idsupervisor', 'fechaInicio']
      widgets = {
         'idimplemento': forms.Select(attrs={'class':'form-select', 'id':'txtImplemento'}),
         'idsupervisor': forms.Select(attrs={'class':'form-select', 'id':'txtSupervisor'}),
         'fechaInicio': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'id':'txtFechainicio', 'min':fecha_actual}),
      }
