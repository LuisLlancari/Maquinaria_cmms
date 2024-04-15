from django.urls import path
#from . import views
from .log import ceco_view, responsable_view

urlpatterns = [
    #Urls de ceco
    path('', ceco_view.ceco, name='ceco'),
    path('registrar_ceco', ceco_view.registrar_ceco, name='registrar_ceco'),
    path('editar_ceco', ceco_view.editar_ceco, name='editar_ceco'),
    path('eliminar_ceco/<int:id_ceco>', ceco_view.eliminar_ceco, name='eliminar_ceco'),


    #Urls de responsable
    path('responsable', responsable_view.responsable, name='responsable'),
    path('registrar_responsable',responsable_view.registrar_responsable, name='registrar_responsable'),
    path('editar_responsable',responsable_view.editar_responsable, name='editar_responsable'),
    path('eliminar_responsable/<int:id_responsable>', responsable_view.eliminar_responsable, name='eliminar_responsable'),
]