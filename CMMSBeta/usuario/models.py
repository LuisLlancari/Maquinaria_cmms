from django.db import models
from django.contrib.auth.models import AbstractUser


class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    rol = models.CharField(unique=True, max_length=30, verbose_name="Rol")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.rol


class Usuario(AbstractUser):
    idrol = models.ForeignKey(Rol, on_delete=models.PROTECT, verbose_name="Rol", null=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
