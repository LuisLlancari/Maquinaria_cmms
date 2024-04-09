from django.db import models
from usuario.models import Usuario

class TipoTractor(models.Model):
    idtipotractor = models.AutoField(primary_key=True)
    tipotractor = models.CharField(max_length=50, verbose_name='Tipo Tractor')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    
    class Meta:
        verbose_name = "Tipo Tractor"
        verbose_name_plural = "Tipos Tractores"
        
    def __str__(self):
        return self.tipotractor
    
class Tractor(models.Model):
    idtractor = models.AutoField(primary_key=True)
    idtipotractor = models.ForeignKey(TipoTractor, on_delete=models.PROTECT, verbose_name='Tipo Tractor', null=True)
    #idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    nrotractor = models.IntegerField(verbose_name='Número Tractor')
    horainicial = models.IntegerField(verbose_name='Hora Inicial')
    horauso = models.IntegerField(verbose_name='Hora Uso')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    
    class Meta:
        verbose_name = "Tractor"
        verbose_name_plural = "Tractores"
        
    def __str__(self):
        return str(self.nrotractor)
    
class ReporteTractor(models.Model):
    idreportetractor = models.AutoField(primary_key=True)
    #idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    horometroinicial = models.IntegerField(verbose_name='Horómetro Inicial')
    horometrofinal = models.IntegerField(verbose_name='Horómetro Final')
    correlativo = models.IntegerField(verbose_name='Correlativo')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    
    class Meta:
        verbose_name = "Reporte Tractor"
        verbose_name_plural = "Reportes Tractores"
        
    def __str__(self):
        return str(self.idreportetractor)
