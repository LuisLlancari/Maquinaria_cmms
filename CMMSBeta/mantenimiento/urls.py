from django.urls import path
#from . import views
from .views import mantenimiento, mantenimiento_preventivo

urlpatterns = [
    #Urls de mantenimiento preventivo
    path('', mantenimiento_preventivo.mantenimiento_preventivo, name='mantenimiento_preventivo'),

    #Urls de mantenimiento
    path('mantenimiento', mantenimiento.mantenimiento, name='mantenimiento'),
    path('mantenimiento/regisrar', mantenimiento.mantenimiento, name='mantenimiento'),
    path('mantenimiento/obtener', mantenimiento.mantenimiento, name='mantenimiento'),
    path('mantenimiento/modificar/<int:id_mantenimimiento>', mantenimiento.mantenimiento, name='mantenimiento'),

]