from django.contrib import admin
from .models import Sede, Base, Area

# Register your models here.
<<<<<<< HEAD
=======

>>>>>>> BackEnd-Fabian
@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
<<<<<<< HEAD
  readonly_fields= ['estado']
=======
    pass
>>>>>>> BackEnd-Fabian


