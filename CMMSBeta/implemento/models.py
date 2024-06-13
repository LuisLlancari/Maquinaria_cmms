from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from localizacion.models import Area
from ceco.models import Ceco
from componente_pieza.models import ConfiguracionTipoImplemento, Componente, Pieza, DetalleComponente
from usuario.models import Usuario

class TipoImplemento(models.Model):
    idtipoimplemento = models.AutoField(primary_key=True)
    tipoimplemento = models.CharField(max_length=45, verbose_name="Tipo Implemento")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    tiempo_vida = models.IntegerField(verbose_name="Tiempo de vida")
    frecuencia_man = models.IntegerField(verbose_name="Frecuencia de mantenimiento")
    idconfiguracion_implemento = models.ForeignKey(ConfiguracionTipoImplemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Configuracion")

    class Meta:
        verbose_name = "Tipo Implemento"
        verbose_name_plural = "Tipos de Implementos"
        ordering = ['tipoimplemento']

    def __str__(self):
        return self.tipoimplemento
    
class Implemento(models.Model):
    idimplemento = models.AutoField(primary_key=True)
    implemento = models.CharField(max_length=45, verbose_name="Implemento")
    idusuario = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default=None, verbose_name="Encargado")
    horasdeuso = models.FloatField(verbose_name="Horas de uso", default=0)
    codimplemento = models.CharField(max_length=12, verbose_name="Codigo de Implemento")
    mantenimientos = models.IntegerField(default=0, null=True, blank=True, verbose_name="Mantenimientos realizados")
    proximo_mantenimiento = models.IntegerField(default=0, null=True, blank=True, verbose_name="Proximo Mantenimiento") 
    idtipoimplemento = models.ForeignKey(TipoImplemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Tipo Implemento")
    idceco = models.ForeignKey(Ceco, on_delete=models.SET_DEFAULT, default=None,verbose_name="Ceco")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Implemento"
        verbose_name_plural = "Implementos"
        ordering = ['implemento', 'idtipoimplemento',]
    def __str__(self):
        return self.implemento
    

    


class DetImplementos(models.Model):
    iddetalleimplemento = models.AutoField(primary_key=True)
    idimplemento = models.ForeignKey(Implemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
    MRimplemento =  models.IntegerField(verbose_name="Mantenimientos realizados al implemento", default=0)
    MRcomponente = models.IntegerField(verbose_name="Mantenimientos realizados al componente", default=0)
    HUcomponente = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Horas de uso del componente", default=0)
    CRcomponente = models.IntegerField(verbose_name="Cambios realizados al componente", default=0)
    iddetallecomponente = models.ForeignKey(DetalleComponente, on_delete=models.SET_DEFAULT, default=None, verbose_name="Detalle componente")
    cantidadpieza = models.IntegerField(verbose_name="Cantidad de piezas", default=0)
    MRpieza = models.IntegerField(verbose_name="Mantenimientos realizados a la pieza",default=0)
    HUpieza = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Horas de uso de la pieza", default=0)
    CRpieza = models.IntegerField(verbose_name="Cambios realizados a la pieza", default=0)
    estado = models.BooleanField(default=True, verbose_name="Estado")


    class Meta:
        verbose_name = "Detalle Implemento"
        verbose_name_plural = "Detalle Implementos"

    def _str_(self):
        return str(self.iddetalleimplemento)