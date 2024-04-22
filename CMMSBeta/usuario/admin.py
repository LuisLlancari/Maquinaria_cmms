from django.contrib import admin
from . models import Usuario, Rol, Persona

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
  pass

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
  pass
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
  pass