from django.contrib import admin
from . models import Componente, Sistema, Pieza, ConfiguracionTipoImplemento, DetalleConfiguracion, DetalleComponente

@admin.register(Componente)
class componeneteAdmin(admin.ModelAdmin):
  list_display=['componente', 'codcomponente', 'tiempovida','frecuencia_man']
  readonly_fields= ['estado']
  
@admin.register(Sistema)
class sistemaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Pieza)
class piezaAdmin(admin.ModelAdmin):
  list_display = [ 'pieza', 'frecuencia_man', 'tiempovida']
  readonly_fields= ['estado']

@admin.register(ConfiguracionTipoImplemento)
class ConfiguracionTipoImplementoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(DetalleConfiguracion)
class DettaleConfiguracionAdmin(admin.ModelAdmin):
  list_display= ['iddetallecomponente','idconfiguracion','idcomponente']
  readonly_fields= ['estado']

@admin.register(DetalleComponente)
class DetalleComponenteAdmin(admin.ModelAdmin):
  list_display = ['iddetallecomponente', 'idcomponente', 'idpieza', 'cantidad',]
  readonly_fields = ['estado']

