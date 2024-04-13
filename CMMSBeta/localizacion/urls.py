from django.urls import path, include
from .views import sede, area, base

urlpatterns = [
    #diretorio
    path('', area.area, name='area'),
    path('base', base.base, name='base'),
    path('sede', sede.sede , name='sede'),
    
    #funciones sede
    path('eliminar_sede/<int:idsede>', sede.eliminar_sede, name='eliminar_sede'), 
    path('registrar_sede', sede.registrar_sede, name='registrar_sede'), 
    path('editar_sede', sede.editar_sede, name='editar_sede'), 
    
    #funciones de base
    path('eliminar_base/<int:idbase>', base.eliminar_base, name='eliminar_base'), 
    path('registrar_base', base.registrar_base, name='registrar_base'), 
    path('editar_base', base.editar_base, name='editar_base'),
    
    #funciones de area
    path('eliminar_area/<int:idarea>', area.eliminar_area, name='eliminar_area'), 
    path('registrar_area', area.registrar_area, name='registrar_area'), 
    path('editar_area', area.editar_area, name='editar_area'),
]