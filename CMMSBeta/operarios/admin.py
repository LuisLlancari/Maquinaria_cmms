from django.contrib import admin
from . models import Solicitante, TipoSolicitante, Tractorista

@admin.register(Solicitante)
class solicitanteAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']


@admin.register(TipoSolicitante)
class TipoSolicitanteAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']


@admin.register(Tractorista)
class TractoristaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']
