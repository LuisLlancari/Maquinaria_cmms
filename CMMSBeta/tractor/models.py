from django.db import models
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.db import models
from fundo_cultivo.models import Cultivo

class TipoTractor(models.Model):
    idtipotractor = models.AutoField(primary_key=True)
    TipoTractor = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.TipoTractor

    
class Tractor(models.Model):
    idtractor = models.AutoField(primary_key=True)
    idtipotractor = models.ForeignKey(TipoTractor, on_delete=models.PROTECT, verbose_name='Tipo Tractor')
    idusuario = models.ForeignKey('usuario.Usuario', on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    idcultivo = models.ForeignKey(Cultivo, on_delete=models.PROTECT, verbose_name='Cultivo', null=True)
    nrotractor = models.CharField(max_length=100 , verbose_name='Nombre Tractor', unique=True)
    horainicial = models.IntegerField(verbose_name='Hora Inicial')
    horauso = models.IntegerField(verbose_name='Hora Uso')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")
    
    class Meta:
        verbose_name = "Tractor"
        verbose_name_plural = "Tractores"
        
    def __str__(self):
        return str(self.nrotractor)
    
class ReporteTractor(models.Model):
    idreportetractor = models.AutoField(primary_key=True)
    #idprogramacion = models.ForeignKey(Programacion, on_delete=models.PROTECT, verbose_name='Programacion', null=True)
    idusuario = models.ForeignKey('usuario.Usuario', on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    idprogramacion = models.ForeignKey('programacion_labor.Programacion', on_delete=models.PROTECT, null=False)
    horometroinicial = models.IntegerField(verbose_name='Horómetro Inicial')
    horometrofinal = models.IntegerField(verbose_name='Horómetro Final')
    correlativo = models.IntegerField(unique=True,verbose_name='Correlativo')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    
    class Meta:
        verbose_name = "Reporte Tractor"
        verbose_name_plural = "Reportes Tractores"
        
    def __str__(self):
        return str(self.idreportetractor)
