from django.db import models


# Create your models here.
class Sede(models.Model):
    idsede = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=50, verbose_name='Sede')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return self.sede

class Base(models.Model):
    idbase = models.AutoField(primary_key=True)
    idsede = models.ForeignKey(Sede, on_delete=models.PROTECT, verbose_name='Sede')
    base = models.CharField(max_length=50, verbose_name='Base')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = "Base"
        verbose_name_plural = "Bases"

    def __str__(self):
        return self.base


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    idbase = models.ForeignKey(Base, on_delete=models.PROTECT)
    area = models.CharField(max_length=50, verbose_name='Area')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Area"

    def __str__(self):
        return self.area
