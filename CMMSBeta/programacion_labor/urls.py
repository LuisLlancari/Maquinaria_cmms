from django.urls import path
#from . import views
from .log import detallelabor_view, programacion_view, tipolabor_view

urlpatterns = [


    #Urls de tipo labor
    path('tipolabor', tipolabor_view.tipolabor, name='tipolabor'),
    path('registrar_tipolabor', tipolabor_view.registrar_tipolabor, name='registrar_tipolabor'),
    path('editar_tipolabor', tipolabor_view.editar_tipolabor, name='editar_tipolabor'),
    path('eliminar_tipolabor/<int:id_tipolabor>', tipolabor_view.eliminar_tipolabor, name='eliminar_tipolabor'),


    #Urls de programacion
    path('programacion', programacion_view.programacion, name='programacion'),
    path('registrar_programacion', programacion_view.registrar_programacion, name='registrar_programacion'),

    #Urls de detalle labor
    path('detallelabor', detallelabor_view.detallelabor, name='detallelabor'),
]