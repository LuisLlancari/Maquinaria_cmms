from django.contrib import admin
from . models import Componente, Sistema, Pieza, DetalleComponente, ConfiguracionTipoImplemento, DetalleConfiguracion

@admin.register(Componente)
class componeneteAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']
  
@admin.register(Sistema)
class sistemaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Pieza)
class piezaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(DetalleComponente)
class DetalleComponenteAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(ConfiguracionTipoImplemento)
class ConfiguracionTipoImplementoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(DetalleConfiguracion)
class DetalleConfiguracionAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

