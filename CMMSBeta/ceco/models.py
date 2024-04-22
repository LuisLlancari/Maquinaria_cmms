from django.db import models

class Ceco(models.Model):
    idceco = models.AutoField(primary_key=True)
    ceco = models.CharField(max_length=30, unique=True, verbose_name='Ceco')
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Ceco'
        verbose_name_plural = 'Cecos'

    def __str__(self):
        return self.ceco
