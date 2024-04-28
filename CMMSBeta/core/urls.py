from django.urls import path, include
from . import views
from .view import reportes

urlpatterns = [
   path('', views.home, name="home"),
   path('home/<datagrafic>/', views.home, name='home_with_datagrafic'),
   path('test', views.test, name="test"),
   path('Exportar', reportes.exportar, name="exportar"),
   path('exportpdf', reportes.reportePDF, name="exportpdf"),
   path('reporteGrafico', reportes.reporteGrafico, name="reporteGrafico"),
]
