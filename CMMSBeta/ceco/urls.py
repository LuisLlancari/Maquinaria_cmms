from django.urls import path
#from . import views
from .log import ceco_view, responsable_view

urlpatterns = [
    #Urls de ceco
    path('', ceco_view.ceco, name='ceco'),
    path('registrar_ceco', ceco_view.registrar_ceco, name='registrar_ceco'),
    path('editar_ceco', ceco_view.editar_ceco, name='editar_ceco'),
    path('eliminar_ceco/<int:id_ceco>', ceco_view.eliminar_ceco, name='eliminar_ceco'),
]