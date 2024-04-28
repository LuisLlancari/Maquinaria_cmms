from django.db import models

class Sistema(models.Model):
    idsistema = models.AutoField(primary_key=True)
    sistema = models.CharField(unique=True, max_length=45, verbose_name="Sistema")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['sistema']
    def __str__(self):
        return self.sistema
    

class Componente(models.Model):
    idcomponente = models.AutoField(primary_key=True)
    idsistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, verbose_name="Sistema")
    componente = models.CharField(max_length=45, verbose_name="Componente")
    codcomponente = models.CharField(max_length=12, verbose_name=("Código componente"))
    tiempovida = models.IntegerField(verbose_name="Tiempo de vida")
    frecuencia_man = models.IntegerField(verbose_name="Frecuencia de mantenimiento", null=True, blank=True) 
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"
        ordering = ['componente']
    def __str__(self):
        return self.componente
    
class Pieza(models.Model):
    idpieza = models.AutoField(primary_key=True)
    pieza = models.CharField(max_length=45, verbose_name="Pieza")
    codpieza = models.CharField(max_length=12, verbose_name="Codigo de pieza")
    tiempoinstalacion = models.IntegerField(verbose_name="Tiempo de instalacion")
    tiempovida = models.IntegerField(verbose_name="Tiempo de vida")
    frecuenciaMP = models.IntegerField(verbose_name="Frecuencia de mantenimiento de pieza")
    idcomponente = models.ForeignKey(Componente, on_delete=models.SET_DEFAULT, default=None, verbose_name="Componenete")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pieza"
        verbose_name_plural = "Piezas"
        ordering = ['pieza', 'idcomponente']
    def __str__(self):
        return self.pieza


