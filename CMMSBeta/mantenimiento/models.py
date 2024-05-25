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
  
  class Meta:
    verbose_name = "Mantenimiento"
    verbose_name_plural = "Mantenimientos"

  def _str_(self):
      return str(self.idmantenimiento)

class ProgramacionMantenimiento(models.Model):
  idprogramacionmantenimiento = models.AutoField(primary_key=True)
  fechaprogramacion = models.DateField(auto_now=False, auto_now_add=False, null=True, blank= True,verbose_name="Fecha mantenimiento")
  idimplemento = models.ForeignKey(Implemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  class Meta:
    verbose_name = "Programacion Mantenimiento"
    verbose_name_plural = "Programacion de Mantenimientos"

  def _str_(self):
      return str(self.idprogramacionmantenimiento)
  
class Diagnostico(models.Model):
  iddiagnostico = models.AutoField(primary_key=True)
  diagnostico = models.CharField(max_length=45, verbose_name="Diagnostico")
  det = models.CharField(max_length=60)

  class Meta:
    verbose_name = "Diagnostico"
    verbose_name_plural = "Diagnosticos"

  def _str_(self):
    return str(self.iddiagnostico)