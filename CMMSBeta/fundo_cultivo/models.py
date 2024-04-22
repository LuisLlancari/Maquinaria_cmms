from django.db import models
from localizacion.models import Sede


class Fundo(models.Model):
    idfundo = models.AutoField(primary_key=True)
    idsede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, verbose_name="Sede")
    fundo = models.CharField(max_length=30, unique=True, verbose_name='Fundo')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Fundo'
        verbose_name_plural = 'Fundos'

    def __str__(self):
        return self.fundo


class Cultivo(models.Model):
    idcultivo = models.AutoField(primary_key=True)
    cultivo = models.CharField(max_length=30, unique=True, verbose_name='Cultivo')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'

    #DEVUELVE EL NOMBRE
    def __str__(self):
        return self.cultivo
    

    
class Variedad(models.Model):
    idvariedad = models.AutoField(primary_key=True)
    variedad = models.CharField(max_length=30, unique=True, verbose_name='Variedad')
    idcultivo = models.ForeignKey(Cultivo, on_delete=models.SET_NULL, null=True, verbose_name="Cultivo")
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Variedad'
        verbose_name_plural = 'Variedades'

    def __str__(self):
        return self.variedad
    

class Lote(models.Model):
    idlote = models.AutoField(primary_key=True)
    idvariedad = models.ForeignKey(Variedad, on_delete=models.SET_NULL, null=True, verbose_name="Variedad")
    idfundo = models.ForeignKey(Fundo, on_delete=models.SET_NULL, null=True, verbose_name="Fundo")
    lote = models.CharField(max_length=30, unique=True, verbose_name='Lote')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return self.lote
    
