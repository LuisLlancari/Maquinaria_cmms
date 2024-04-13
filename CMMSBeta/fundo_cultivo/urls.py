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

  #Urls de variedad
  path('variedad', variedad_view.variedad , name='variedad'),

  #Urls de lote
  path('lote', lote_view.lote , name='lote'),
]