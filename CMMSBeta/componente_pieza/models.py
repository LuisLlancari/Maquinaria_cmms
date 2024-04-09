from django.db import models

class Sistema(models.Model):
    idSistema = models.AutoField(primary_key=True)
    sistema = models.CharField(unique=True, max_length=45, verbose_name="Sistema")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['sistema']
    def __str__(self):
        return self.sistema

class Componente(models.Model):
    idComponente = models.AutoField(primary_key=True)
    componente = models.CharField(max_length=45, verbose_name="Componente")
    codComponente = models.CharField(max_length=12, verbose_name=("Código componente"))
    horaInstalacion = models.IntegerField("Hora Instalacion")
    tiempoVida = models.IntegerField(verbose_name="Tiempo de vida")
    idSistema = models.ForeignKey(Sistema, on_delete=models.SET_DEFAULT, default=None, verbose_name="Sistema")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creadoEn = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizadoEn = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"
        ordering = ['componente', 'idSistema']
    def __str__(self):
        return self.componente

class Pieza(models.Model):
    idPieza = models.AutoField(primary_key=True)
    pieza = models.CharField(max_length=45, verbose_name="Pieza")
    codPieza = models.CharField(max_length=12, verbose_name="Codigo de pieza")
    tiempoInstalacion = models.IntegerField(verbose_name="Tiempo de instalacion")
    tiempoVida = models.IntegerField(verbose_name="Tiempo de vida")
    frecuenciaMP = models.IntegerField(verbose_name="Frecuencia de mantenimiento de pieza")
    idComponente = models.ForeignKey(Componente, on_delete=models.SET_DEFAULT, default=None, verbose_name="Componenete")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creadoEn = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizadoEn = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pieza"
        verbose_name_plural = "Piezas"
        ordering = ['pieza', 'idComponente']
    def __str__(self):
        return self.pieza
