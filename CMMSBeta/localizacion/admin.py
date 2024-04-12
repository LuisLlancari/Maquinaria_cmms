from django.contrib import admin
from .models import Sede, Base, Area

# Register your models here.
@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
'''
@admin.register(admin.Base)

class BaseAdmin(admin.ModelAdmin):
    pass

@admin.register(admin.Area)
class AreaAdmin(admin.ModelAdmin):
    pass
'''
