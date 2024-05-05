from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45, verbose_name="Nombres")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    dni = models.CharField(max_length=8, unique=True, null=True, blank=True, verbose_name="DNI")
    codigo = models.CharField(max_length=12, null=True, verbose_name="Codigo")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def save(self, *args, **kwargs):
        if not self.codigo:  # Si el código no está establecido
            last_persona = Persona.objects.order_by('-codigo').first()  # Obtener el último registro
            if last_persona:  # Si hay registros existentes
                last_codigo = int(last_persona.codigo)
                self.codigo = str(last_codigo + 1)  # Incrementar el código en 1
            else:
                self.codigo = "1000"  # Si no hay registros, empezar en 1000
        super().save(*args, **kwargs)




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

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id}"

    
