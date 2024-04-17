from django.contrib import admin
from .models import TipoTractor, Tractor, ReporteTractor

# Register your models here.

@admin.register(TipoTractor)
class TipotractorAdmin(admin.ModelAdmin):
    pass

@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    pass

@admin.register(ReporteTractor)
class ReportetractorAdmin(admin.ModelAdmin):
     pass