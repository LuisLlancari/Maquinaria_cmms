from django.contrib import admin
from .models import *


admin.site.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

admin.site.register(ProgramacionMatenimiento)
class ProgramacionMatenimientoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']