from django import forms
from .models import Fundo, Cultivo, Variedad, Lote

class VariedadChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.variedad} - {obj.idcultivo.cultivo}"

class FundoForm(forms.ModelForm):
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
    class Meta:
        model = Variedad
        fields = ['variedad', 'idcultivo']
        widgets = {
            'variedad': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idcultivo': forms.Select(attrs={'class': 'form-control mb-2'}),
        }

class LoteForm(forms.ModelForm):
    idvariedad = VariedadChoiceField(queryset=Variedad.objects.all(), label="Variedad - Cultivo")

    class Meta:
        model = Lote
        fields = ['lote', 'idvariedad','idfundo']
        widgets = {
            'lote': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'idfundo': forms.Select(attrs={'class': 'form-control mb-2'}),
            'idvariedad': forms.Select(attrs={'class': 'form-select mb-2 mt-2'}),
        }
