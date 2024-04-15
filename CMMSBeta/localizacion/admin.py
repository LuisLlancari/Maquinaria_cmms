from django.contrib import admin
from .models import Sede, Base, Area

# Register your models here.
@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']


