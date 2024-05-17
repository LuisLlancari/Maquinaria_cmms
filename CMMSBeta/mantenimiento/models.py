from usuario.models import Persona
from implemento.models import Implemento
from django.db import models

class Mantenimiento(models.Model):
  idmantenimiento = models.AutoField(primary_key=True)
  tipomantenimiento = models.CharField(max_length=45, verbose_name="Tipo mantenimiento")
  fechaingreso = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha Ingreso')
  fechasalida = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha Fecha Salida")
  descripcion = models.CharField(max_length=45, verbose_name="Descripcion")
  persona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
  estado = models.BooleanField(default=True, verbose_name="Estado")

class ProgramacionMantenimiento(models.Model):
  idprogramacionmantenimiento = models.AutoField(primary_key=True)
  fechaprogramacion = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha Fecha Salida")
  idimplemento = models.ForeignKey(Implemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
  estado = models.BooleanField(default=True, verbose_name="Estado")

class Diagnostico(models.Model):
  iddiagnostico = models.AutoField(primary_key=True)
  diagnostico = models.CharField(max_length=45, verbose_name="Diagnostico")
  det = models.CharField(max_length=60)