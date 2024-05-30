from django.contrib import admin
from mantenimiento.models import Mantenimiento, ProgramacionMantenimiento, Acciones, DetMotivos, DetalleCambios, DetalleMantenimiento
# Register your models here.
@admin.register(ProgramacionMantenimiento)
class ProgramacionMantenimientoAdmin(admin.ModelAdmin):
  list_display = ['idprogramacionmantenimiento','idimplemento', 'fechaprogramacion']
  readonly_fields = ['estado']

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
  readonly_fields = ['estado']

@admin.register(Acciones)
class AccionesAdmin(admin.ModelAdmin):
  list_display = ['idaccion', 'accion', 'estado']

@admin.register(DetMotivos)
class DetMotivosAdmin(admin.ModelAdmin):
  list_display = ['idprogramacionmantenimiento', 'idaccion']

@admin.register(DetalleCambios)
class DetalleCambiosAdmin(admin.ModelAdmin):
  readonly_fields=['estado']

@admin.register(DetalleMantenimiento)
class DetalleMantenimientoAdmin(admin.ModelAdmin):
  readonly_fields=['estado']