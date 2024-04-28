from django.db import models
from usuario.models import Usuario, Persona
from componente_pieza.models import Pieza


from implemento.models import DetImplementos

# Create your models here.
class ProgramacionMatenimiento(models.Model):
    idprogramacionmantenimiento = models.AutoField(primary_key=True)
    detimplemento = models.ForeignKey(DetImplementos, on_delete=models.SET_DEFAULT, default=None, verbose_name="Detimplemento")
    fechaprogramacion = models.DateField(verbose_name="Fecha Programacion", null=True, blank=True)
    contadormantenimiento = models.IntegerField(verbose_name="Contador Mantenimiento")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    
    class Meta:
          verbose_name = "Porgramacion Mantenimiento"
          verbose_name_plural = "Programaciones Mantenimientos"

    def _str_(self):
      return str(self.idmanpreventivo)

    
class Mantenimiento(models.Model):
    TIPOSMANTENIMIENTO_CHOICES = (
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),  # Corregido el valor de esta opción
    )
    
    idmantenimiento = models.AutoField(primary_key=True)
    idprogramacionmantenimiento = models.ForeignKey(ProgramacionMatenimiento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Programacion mantenimiento")
    fechaingreso = models.DateField(null=True, blank=True, verbose_name="Fecha de Ingreso")
    fechasalida = models.DateField(null=True, blank=True, verbose_name="Fecha de Salida")
    descripcion = models.CharField(max_length=60, verbose_name="Descripcion")
    idpersona = models.ForeignKey(Persona, on_delete=models.SET_DEFAULT, default=None, verbose_name="Persona")
    tipomantenimiento = models.CharField(max_length=20, choices=TIPOSMANTENIMIENTO_CHOICES, verbose_name="Tipo de mantenimiento", default='preventivo')  # Se define un valor predeterminado
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
          verbose_name = "Mantenimiento"
          verbose_name_plural = "Mantenimientos"

    def __str__(self):
        return str(self.idmantenimiento)
    
    
class Diagnostico(models.Model):
    iddiagnostico = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=60, verbose_name="Diagnostico")
    idmantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.SET_DEFAULT, default=None, verbose_name="idmantenimiento")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
          verbose_name = "Diagnostico"
          verbose_name_plural = "Diagnosticos"

    def __str__(self):
      return str(self.iddiagnostico)
    

class DetalleDiagnostico(models.Model):
    iddetallediagnostico = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=45, verbose_name="Motivo")
    sugerencia = models.CharField(max_length=45, verbose_name="Sugerencia")
    iddiagnostico = models.ForeignKey(Diagnostico,on_delete=models.SET_DEFAULT, default=None, verbose_name="idiagnostico")
    idpieza = models.ForeignKey(Pieza, on_delete=models.SET_DEFAULT, default=None, verbose_name="Pieza")