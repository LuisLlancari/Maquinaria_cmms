from django.db import models
from usuario.models import Usuario, Persona


from implemento.models import DetImplementos

# Create your models here.
class MantenimientoPreventivo(models.Model):
    idmanpreventivo = models.AutoField(primary_key=True)
    detimplemento = models.ForeignKey(DetImplementos, on_delete=models.SET_DEFAULT, default=None, verbose_name="Detimplemento")
    fechaprogramacion = models.DateField(verbose_name="Fecha Programacion")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    
    class Meta:
          verbose_name = "Mantenimiento Preventivo"
          verbose_name_plural = "Mantenimientos Preventivos"

    def __str__(self):
      return str(self.idmanpreventivo)
    
class Mantenimiento(models.Model):
    idmantenimiento = models.AutoField(primary_key=True)
    idmanpreventivo = models.ForeignKey(MantenimientoPreventivo , on_delete=models.SET_DEFAULT, default=None, verbose_name="mantenimiento preventivo")
    fechasalida = models.DateField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
    idpersona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
    descripcion = models.CharField(max_length=60, verbose_name="Descripcion")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
          verbose_name = "Mantenimiento"
          verbose_name_plural = "Mantenimientos"

    def __str__(self):
      return str(self.idmantenimiento)
