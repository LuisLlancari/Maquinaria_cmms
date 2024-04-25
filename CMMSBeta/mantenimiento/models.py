from django.db import models
from usuario.models import Usuario, Persona


# Create your models here.
class Mantenimiento(models.Model):
  idmantenimiento = models.AutoField(primary_key=True)
  idmanpreventivo = models.ForeignKey( , on_delete=models.SET_DEFAULT, default=None, verbose_name="mantenimiento preventivo")
  fechasalida = models.DateField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
  idpersona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
  descripcion = models.CharField(max_length=60, verbose_name="Descripcion")
  estado = models.BooleanField(default=True, verbose_name="Estado")

  class Meta:
          verbose_name = "Mantenimiento"
          verbose_name_plural = "Mantenimientos"

  def __str__(self):
      return self.idmantenimiento
