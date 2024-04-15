from django.contrib import admin
<<<<<<< HEAD
from .models import Ceco, Responsable

@admin.register(Responsable)
class responsableAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

@admin.register(Ceco)
class cecoAdmin(admin.ModelAdmin):
  readonly_fields= ['estado']

=======
from .models import Ceco , Responsable


@admin.register(Ceco)
class CecoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']

@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
>>>>>>> Backend-Harold
