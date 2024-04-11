from django.contrib import admin
from .models import Ceco , Responsable


@admin.register(Ceco)
class CecoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
