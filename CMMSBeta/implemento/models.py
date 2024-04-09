from django.db import models

class TipoImplemento(models.Model):
    idTipoimplemento = models.AutoField(primary_key=True)
    tipoImplemento = models.CharField(unique=True, max_length=45, verbose_name="Tipo Implemento")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Tipo Implemento"
        verbose_name_plural = "Tipos de Implementos"
        ordering = ['tipoImplemento']

    def __str__(self):
        return self.tipoImplemento

class Implemento(models.Model):
    idImplemento = models.AutoField(primary_key=True)
    implemento = models.CharField(max_length=45, verbose_name="Implemento")
    tiempoVida = models.IntegerField(verbose_name="Tiempo de vida")
    nroImplemento = models.CharField(max_length=12, verbose_name="Numero de Implemento")
    horasDeUso = models.IntegerField(verbose_name="Horas de Uso")
    codImplimento = models.CharField(max_length=12, verbose_name="Codigo de Implemento")
    idTipoimplemento = models.ForeignKey(TipoImplemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Tipo Implemento")
    idArea = models.ForeignKey(Areamodel, on_delete=models.SET_DEFAULT, default=None, verbose_name="Area")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creadoEn = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizadoEn = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Implemento"
        verbose_name_plural = "Implementos"
        ordering = ['implemento', 'idTipoimplemento',]
    def __str__(self):
        return self.implemento

class Responsable(models.Model):
    idResponsable = models.AutoField(primary_key=True)
    responsable = models.CharField(max_length=40, blank=True, null=True, verbose_name="Responsable")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        ordering = ['responsable']
    def __str__(self):
        return self.responsable

class DetImplementos(models.Model):
    idDetalleimplemento = models.AutoField(primary_key=True)
    idResponsable = models.ForeignKey(Responsable, on_delete=models.SET_DEFAULT, default=None, verbose_name="Responsable")
    idPieza = models.ForeignKey(Piezamodel, on_delete=models.SET_DEFAULT, default=None, verbose_name="Pieza")
    idCeco = models.ForeignKey(Cecomodel, on_delete=models.SET_DEFAULT, default=None, verbose_name="CECO")
    idImplemento = models.ForeignKey(Implemento, on_delete=models.SET_DEFAULT, default=None, verbose_name="Implemento")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creadoEn = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizadoEn = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Detalle Implemento"
        verbose_name_plural = "Detalle Implementos"
        ordering = ['idPieza', 'idResponsable', 'creadoEn']