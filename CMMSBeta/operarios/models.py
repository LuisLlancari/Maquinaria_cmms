from django.db import models
from usuario.models import Usuario

class TipoSolicitante(models.Model):
    idtiposolicitante = models.AutoField(primary_key=True)
    tiposolicitante = models.CharField(unique=True, max_length=45, verbose_name="Tipo Solicitante")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Tipo Solicitante"
        verbose_name_plural = "Tipos de Solicitantes"
        ordering = ['tiposolicitante']

    def __str__(self):
        return self.tiposolicitante
    
class Solicitante(models.Model):
    idsolicitante = models.AutoField(primary_key=True)
    idtiposolicitante = models.ForeignKey(TipoSolicitante, on_delete=models.SET_DEFAULT, default=None,verbose_name="Tipo Solicitante")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    nombres = models.CharField(max_length=45, verbose_name="Nombres")
    codigo =  models.CharField(max_length=12, verbose_name="Codigo")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"
        ordering = ['idsolicitante', 'idtiposolicitante']
    
    def __str__(self):
        return self.codigo
    
class Tractorista(models.Model):
    idtractorista = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('usuario.Usuario', on_delete=models.SET_DEFAULT, default=None, verbose_name="Usuario")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    nombres = models.CharField(max_length=45, verbose_name="Nombres")
    codigo =  models.CharField(max_length=12, verbose_name="Codigo")
    dni =  models.CharField(max_length=8, verbose_name="DNI")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")

    class Meta:
        verbose_name = "Tractorista"
        verbose_name_plural = "Tractoristas"
        ordering = ['idtractorista', 'apellidos']

    def __str__(self):
        return self.codigo