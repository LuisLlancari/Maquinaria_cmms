from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('test', views.test, name="test"),
   path('Exportar', views.exportar, name="exportar"),
   path('exportpdf', views.reportePDF, name="exportpdf"),
]
