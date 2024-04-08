from django.contrib import admin
from . models import Usuario

@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
  pass
