from django.contrib import admin
from .models import Fundo

@admin.register(Fundo)
class FundoAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
