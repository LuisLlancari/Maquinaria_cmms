from django.db import models
from fundo_cultivo.models import Lote
from tractor.models import Tractor
from operarios.models import Tractorista, Solicitante
from implemento.models import Implemento
from django.contrib.auth.models import User
from usuario.models import Usuario


class TipoLabor(models.Model):
    idtipolabor = models.AutoField(primary_key=True)
    tipolabor = models.CharField(max_length=30, unique=True, verbose_name='Tipo de labor')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Tipo de labor'
        verbose_name_plural = 'Tipos de labor'

    def __str__(self):  
        return self.tipolabor
    
class Programacion(models.Model):

    TURNO_CHOICES = (
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )

    idprogramacion = models.AutoField(primary_key=True)
    idtipolabor = models.ForeignKey(TipoLabor, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de labor")
    idlote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, verbose_name="Lote")
    idtractor = models.ForeignKey(Tractor, on_delete=models.SET_NULL, null=True, verbose_name="Tractor")
    idusuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    idtractorista = models.ForeignKey(Tractorista, on_delete=models.SET_NULL, null=True, verbose_name="Tractorista")
    idsolicitante = models.ForeignKey(Solicitante, on_delete=models.SET_NULL, null=True, verbose_name="Solicitante")
    fechahora = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha')
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES, verbose_name="Turno")
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'

    def __str__(self):
        return self.idprogramacion
    
class DetalleLabor(models.Model):
    iddetlabor = models.AutoField(primary_key=True)
    idimplemento = models.ForeignKey(Implemento, on_delete=models.SET_NULL, null=True, verbose_name="Implemento")
    idprogramacion = models.ForeignKey(Programacion, on_delete=models.SET_NULL, null=True, verbose_name="Programacion")
    horadeuso = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Hora de uso Implemento')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Detalle Labor'
        verbose_name_plural = 'Detalles de labor'

    def __str__(self):
        return self.iddetlabor
    

