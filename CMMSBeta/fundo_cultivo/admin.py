from django.contrib import admin
from .models import Fundo, Cultivo, Variedad, Lote

@admin.register(Fundo)
class FundoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Variedad)  
class VariedadAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

