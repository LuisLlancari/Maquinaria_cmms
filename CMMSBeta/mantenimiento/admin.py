from django.contrib import admin
from mantenimiento.models import Mantenimiento, ProgramacionMantenimiento
# Register your models here.
@admin.register(ProgramacionMantenimiento)
class ProgramacionMantenimientoAdmin(admin.ModelAdmin):
  list_display = ['idprogramacionmantenimiento','idimplemento', 'fechaprogramacion']
  readonly_fields = ['estado']

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
  readonly_fields = ['estado']