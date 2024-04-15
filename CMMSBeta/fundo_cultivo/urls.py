from django.urls import path
#from . import views
from .log import fundo_view, lote_view, cultivo_view, variedad_view

urlpatterns = [
  #Urls de fundo
  path('fundo', fundo_view.fundo , name='fundo'),
  path('registrar_fundo', fundo_view.registrar_fundo , name='registrar_fundo'),
  path('eliminar_fundo/<int:id_fundo>', fundo_view.eliminar_fundo , name='eliminar_fundo'),
  path('editar_fundo', fundo_view.editar_fundo , name='editar_fundo'),

  #Urls de lote
  path('cultivo', cultivo_view.cultivo , name='cultivo'),
  path('registrar_cultivo', cultivo_view.registrar_cultivo , name='registrar_cultivo'),
  path('editar_cultivo', cultivo_view.editar_cultivo , name='editar_cultivo'),
  path('eliminar_cultivo/<int:id_cultivo>', cultivo_view.eliminar_cultivo , name='eliminar_cultivo'),

  #Urls de variedad
  path('variedad', variedad_view.variedad , name='variedad'),
  path('registrar_variedad', variedad_view.registrar_variedad , name='registrar_variedad'),
  path('editar_variedad', variedad_view.editar_variedad , name='editar_variedad'),
  path('eliminar_variedad/<int:id_variedad>', variedad_view.eliminar_variedad , name='eliminar_variedad'),

  #Urls de lote
  path('lote', lote_view.lote , name='lote'),
  path('registrar_lote', lote_view.registrar_lote , name='registrar_lote'),
  path('editar_lote', lote_view.editar_lote , name='editar_lote'),
  path('eliminar_lote/<int:id_lote>', lote_view.eliminar_lote , name='eliminar_lote'),
]