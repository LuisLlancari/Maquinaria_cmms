from django.contrib import admin
from .models import Ceco, Responsable

@admin.register(Responsable)
class responsableAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Ceco)
class cecoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

