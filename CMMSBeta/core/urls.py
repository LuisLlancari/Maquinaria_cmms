from django.urls import path, include
from . import views
from .view import reportes

urlpatterns = [
   path('', views.home, name="home"),
   path('home/<datagrafic>/', views.home, name='home_with_datagrafic'),

   path('datos_graficos/<str:fecha>/<int:supervisor>/<str:turnos>', views.datos_grafico, name='datos_grafico'),
   path('datos_tabla/<str:fecha>/<int:supervisor>/<str:turno>', views.datos_tabla, name='datos_tabla'),
   path('datos_tabla_detalle/<str:fecha>/<int:supervisor>/<str:turno>/<int:idfundo>', views.datos_tabla_detalle, name='datos_tabla_detalle'),

   path('test', views.test, name="test"),
   path('Exportar', reportes.exportar, name="exportar"),
   path('exportpdf', reportes.reportePDF, name="exportpdf"),
   path('reporteGrafico', reportes.reporteGrafico, name="reporteGrafico"),
]
