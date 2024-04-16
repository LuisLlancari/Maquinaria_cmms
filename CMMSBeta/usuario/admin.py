from django.contrib import admin
from . models import Usuario, Rol

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
  pass

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
  pass
