from django.contrib import admin
from . models import Implemento, TipoImplemento, DetImplementos 
# Register your models here.

@admin.register(Implemento)
class implementoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']
  list_display = ['implemento', 'horasdeuso', 'idimplemento', 'proximo_mantenimiento']

@admin.register(TipoImplemento)
class tipoimplementoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']


@admin.register(DetImplementos)
class detalleimplementoAdmin(admin.ModelAdmin):
  list_display = ['iddetalleimplemento', 'idimplemento']
  readonly_fields= ['estado']

