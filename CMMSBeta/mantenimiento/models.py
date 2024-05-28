from usuario.models import Persona
from implemento.models import Implemento
from django.db import models

class ProgramacionMantenimiento(models.Model):

  MANTENIMIENTO_CHOICES = (
    (1, 'Preventivo'),
    (0, 'Correctvo')
  )

  idprogramacionmantenimiento = models.AutoField(primary_key=True)
  fechaprogramacion = models.DateField(auto_now=False, auto_now_add=False, null=True, blank= True,verbose_name="Fecha mantenimiento")
  tipomantenimiento = models.IntegerField(choices=MANTENIMIENTO_CHOICES, verbose_name="Tipo mantenimiento", null=True, blank=True)
  idimplemento = models.ForeignKey(Implemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  class Meta:
    verbose_name = "Programacion Mantenimiento"
    verbose_name_plural = "Programacion de Mantenimientos"

  def __str__(self):
      return str(self.idprogramacionmantenimiento)

class Mantenimiento(models.Model):

  idmantenimiento = models.AutoField(primary_key=True)
  idprogramacionmantenimiento = models.ForeignKey(ProgramacionMantenimiento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Programacion" )
  fechaingreso = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Fecha Ingreso')
  fechasalida = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Fecha Fecha Salida")
  descripcion = models.CharField(max_length=45, verbose_name="Descripcion")
  persona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None, verbose_name="Persona")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  
  class Meta:
    verbose_name = "Mantenimiento"
    verbose_name_plural = "Mantenimientos"

  def __str__(self):
      return str(self.idmantenimiento)

  
class Diagnostico(models.Model):
  iddiagnostico = models.AutoField(primary_key=True)
  diagnostico = models.CharField(max_length=45, verbose_name="Diagnostico")
  det = models.CharField(max_length=60)

  class Meta:
    verbose_name = "Diagnostico"
    verbose_name_plural = "Diagnosticos"

  def _str_(self):
    return str(self.iddiagnostico)
  

# Para las acciones
class Acciones(models.Model):
    ESTADO_CHOICES = [
        (0, 'Supervisor'),
        (1, 'Mecánico'),
        (2, 'Ambos'),
    ]

    idaccion = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=45, verbose_name="Acción de mantenimiento", unique=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES, verbose_name="Rol")

    class Meta:
        verbose_name = "Acción"
        verbose_name_plural = "Acciones"

    def __str__(self):
        return self.accion
  
class DetMotivos(models.Model):
  iddetmotivo = models.AutoField(primary_key=True)
  idprogramacionmantenimiento = models.ForeignKey(ProgramacionMantenimiento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Programacion de Mantenmiento")
  idaccion = models.ForeignKey(Acciones, on_delete=models.SET_DEFAULT, default=None, verbose_name="Accion")
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Motivo"
    verbose_name_plural = "Motivos"

  def _str_(self):
    return str(self.iddetmotivo)
  
