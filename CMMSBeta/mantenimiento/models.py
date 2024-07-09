from usuario.models import Persona
from operarios.models import Encargado
from implemento.models import Implemento, DetImplementos, ImplementoSupervisor
from django.db import models

class ProgramacionMantenimiento(models.Model):

  MANTENIMIENTO_CHOICES = (
    (1, 'Preventivo'),
    (0, 'Correctvo')
  )
  ESTADOMANTENIMIENTO_CHOICES = (
  (0, 'Programado'),
  (1, 'Aceptado'),
  (2, 'Finalizado'),
  )

  idprogramacionmantenimiento = models.AutoField(primary_key=True)
  fechaprogramacion = models.DateField(auto_now=False, auto_now_add=False, null=True, blank= True,verbose_name="Fecha mantenimiento")
  tipomantenimiento = models.IntegerField(choices=MANTENIMIENTO_CHOICES, verbose_name="Tipo mantenimiento", null=True, blank=True)
  idimplemento = models.ForeignKey(ImplementoSupervisor, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  estado_mantenimiento = models.IntegerField(choices=ESTADOMANTENIMIENTO_CHOICES, verbose_name="Estado del Mantenimiento", null=True, blank=True, default=0)
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
  idencargado = models.ForeignKey(Encargado, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None, verbose_name="Encargado")
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

  def __str__(self):
    return str(self.iddiagnostico)
  
class Acciones(models.Model):
    ESTADO_CHOICES = [
        (0, 'Supervisor'),
        (1, 'Mecánico'),
        (2, 'Ambos'),
    ]

    idaccion = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=45, verbose_name="Acción de mantenimiento", unique=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES, verbose_name="Rol")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado", null=True, blank=True)

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

  def __str__(self):
    return str(self.iddetmotivo)
  
class DetalleMantenimiento(models.Model):
  iddetallemantenimiento = models.AutoField(primary_key=True)
  idaccion = models.ForeignKey(Acciones,on_delete=models.SET_DEFAULT, default=None, verbose_name="Accion")
  idmantenimiento = models.ForeignKey(Mantenimiento,on_delete=models.SET_DEFAULT, default=None, verbose_name="Mantenimiento")
  completado = models.BooleanField(default=True, verbose_name="Realizado")
  creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  
  class Meta:
    verbose_name = "Detalle Mantenimiento"
    verbose_name_plural = "Detalles de Mantenimientos"

  def __str__(self):
    return str(self.iddetallemantenimiento)
   
class DetalleCambios(models.Model):

  iddetallecambio = models.AutoField(primary_key=True)
  idmantenimiento = models.ForeignKey(Mantenimiento,on_delete=models.SET_DEFAULT, default=None, verbose_name="Mantenimiento")
  iddetalleimplemento = models.ForeignKey(DetImplementos,on_delete=models.SET_DEFAULT, default=None, verbose_name="Mantenimiento")
  creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  class Meta:
    verbose_name = "Detalle Cambio"
    verbose_name_plural = "Detalles de Cambios"

  def __str__(self):
    return str(self.iddetallecambio)
  
class Recambios(models.Model):
  idrecambio = models.AutoField(primary_key=True)
  idmantenimiento = models.ForeignKey(Mantenimiento,on_delete=models.SET_DEFAULT, default=None, verbose_name="Mantenimiento")
  item = models.CharField(max_length=45, verbose_name="Parte del recambio" )
  codigo = models.CharField(max_length=12, verbose_name="Codigo")
  estado = models.BooleanField(default=True, verbose_name="Estado")
  creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  class Meta:
    verbose_name = "Recambio"
    verbose_name_plural = "Recambios"
  def __str__(self):
    return str(self.idrecambio)
