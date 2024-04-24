from django.urls import path, include
from . import views
from .view import reportes

urlpatterns = [
   path('', views.home, name="home"),
   path('test', views.test, name="test"),
   path('Exportar', reportes.exportar, name="exportar"),
   path('exportpdf', reportes.reportePDF, name="exportpdf"),
   path('reporteGrafico', reportes.reporteGrafico, name="reporteGrafico"),
]
