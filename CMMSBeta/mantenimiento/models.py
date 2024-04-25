from django.db import models

from implemento.models import DetImplementos

# Create your models here.

class MantenimientoPreventivo(models.Model):
    idmantenimiento = models.AutoField(primary_key=True)
    detimplemento = models.ForeignKey(DetImplementos, on_delete=models.SET_DEFAULT, default=None, verbose_name="Detimplement")
    fechaprogramacion = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Programacion")
    estado = models.BooleanField(default=True, verbose_name="Estado")
