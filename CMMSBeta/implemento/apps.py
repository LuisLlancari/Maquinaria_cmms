from django.apps import AppConfig


class ImplementoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'implemento'
    
    def ready(self):
        from . import signals