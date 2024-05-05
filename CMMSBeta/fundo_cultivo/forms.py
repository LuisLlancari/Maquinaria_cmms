from django import forms
from .models import Fundo, Cultivo, Variedad, Lote
from localizacion.models import Sede

class VariedadChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.variedad} - {obj.idcultivo.cultivo}"

class FundoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idsede'].queryset = Sede.objects.filter(
            estado=True)
    class Meta:
        model = Fundo
        fields = ['fundo', 'idsede']
        widgets = {
            'fundo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idsede': forms.Select(attrs={'class': 'form-control mb-2'}),
        }

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['cultivo']
        widgets = {
            'cultivo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }

class VariedadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idcultivo'].queryset = Cultivo.objects.filter(
            estado=True)
    class Meta:
        model = Variedad
        fields = ['idcultivo','variedad']
        widgets = {
            'idcultivo': forms.Select(attrs={'class': 'form-control mb-2'}),
            'variedad': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }

class LoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idfundo'].queryset = Fundo.objects.filter(
            estado=True)

    class Meta:
        model = Lote
        fields = ['lote', 'idvariedad','idfundo']
        widgets = {
            'lote': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idfundo': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idvariedad': forms.Select(attrs={'class': 'form-select mb-2 mt-2'}),
        }
