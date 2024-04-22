from django.db import models
from usuario.models import Usuario, Persona

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
    idpersona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")
    creado_en = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, null=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"
        ordering = ['idsolicitante', 'idtiposolicitante']
    
    def __str__(self):
        return f"Solicitante: {self.idpersona.nombres} {self.idpersona.apellidos}"
    

class Tractorista(models.Model):
    idtractorista = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('usuario.Usuario', on_delete=models.SET_DEFAULT, default=None, verbose_name="Usuario")
    idpersona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estado_actividad = models.BooleanField(default=True, verbose_name="Estado Actividad")
    creado_en = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tractorista"
        verbose_name_plural = "Tractoristas"
        ordering = ['idtractorista']

    def __str__(self):
        return f"Tractorista: {self.idpersona.nombres} {self.idpersona.apellidos}"
