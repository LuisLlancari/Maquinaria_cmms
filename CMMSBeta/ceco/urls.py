from django.urls import path
from . import views

urlpatterns = [
    #Urls de ceco
    path('', views.ceco, name='ceco'),
    path('registrar_ceco', views.registrar_ceco, name='registrar_ceco'),
    path('editar_ceco', views.editar_ceco, name='editar_ceco'),
    path('eliminar_ceco/<int:id_ceco>', views.eliminar_ceco, name='eliminar_ceco'),


    #Urls de responsable
    path('responsable', views.responsable, name='responsable'),
    path('registrar_responsable',views.registrar_responsable, name='registrar_responsable'),
    path('editar_responsable',views.editar_responsable, name='editar_responsable'),
    path('eliminar_responsable/<int:id_responsable>', views.eliminar_responsable, name='eliminar_responsable'),
]