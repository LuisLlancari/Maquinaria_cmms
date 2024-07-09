from django.db import models
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.db import models
from fundo_cultivo.models import Cultivo, Fundo

class TipoTractor(models.Model):
    idtipotractor = models.AutoField(primary_key=True)
    TipoTractor = models.CharField(max_length=100, verbose_name="Tipo de tractor")
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.TipoTractor
    
class Tractor(models.Model):
    idtractor = models.AutoField(primary_key=True)
    idtipotractor = models.ForeignKey(TipoTractor, on_delete=models.PROTECT, verbose_name='Tipo Tractor')
    idfundo = models.ForeignKey(Fundo, on_delete=models.PROTECT, verbose_name='Fundo', null=True)
    nrotractor = models.CharField(max_length=100 , verbose_name='Nombre Tractor')
    horainicial = models.IntegerField(verbose_name='Hora Inicial')
    horauso = models.IntegerField(verbose_name='Hora Uso', default=0)
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

class TractorSupervisor(models.Model):
    idtractorsupervisor = models.AutoField(primary_key=True, verbose_name="id")
    idtractor = models.ForeignKey(Tractor,on_delete=models.SET_DEFAULT, default=None, verbose_name="Tractor") 
    idsupervisor = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default=None, verbose_name="Usuario")
    fechaInicio = models.DateField(verbose_name="Fecha Inicio")
    fechaFin = models.DateField(null=True, blank=True,verbose_name="Fecha Fin")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "tractor por supervisor"
        verbose_name_plural = "tractores por supervisores"
    
    def __str__(self):
        return str( self.idtractorsupervisor)