from django.contrib import admin
from . models import Componente, Sistema

@admin.register(Componente)
class componeneteAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']
  

@admin.register(Sistema)
class sistemaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

