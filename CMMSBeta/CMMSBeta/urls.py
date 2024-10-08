"""
URL configuration for CMMSBeta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Importamos el login y logout creados en usuarios
from usuario import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('usuario/', include('django.contrib.auth.urls')),
    path('usuario/', include('usuario.urls')),
    path('implemento/', include('implemento.urls')),
    path('componente/', include('componente_pieza.urls')),
    path('operarios/', include('operarios.urls')),
    path('fundo/', include('fundo_cultivo.urls')),
    path('ceco/', include('ceco.urls')),
    path('programacion/', include('programacion_labor.urls')),
    path('tractor/', include('tractor.urls')),
    path('localizacion/', include('localizacion.urls')),

    # Importamos las vistas del login y logout
    path('login',usuario_views.login_user, name="login"),
    path('logout/',usuario_views.logout_user, name="logout"),

]
