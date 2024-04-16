from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TipoTractor)
class TipoTractorAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
    pass

@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
    pass

@admin.register(ReporteTractor)
class ReportetractorAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']