from django.contrib import admin
from .models import Sede, Base, Area

# Register your models here.

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    pass

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass


