from django.contrib import admin
from .models import Programacion, TipoLabor, DetalleLabor

@admin.register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoLabor)
class TipoLaborAdmin(admin.ModelAdmin):
    pass

@admin.register(DetalleLabor)
class DetalleLaborAdmin(admin.ModelAdmin):
    pass
