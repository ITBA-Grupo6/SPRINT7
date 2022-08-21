"""itbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import include

from Base import views as views_Base
from Clientes import views as views_Clientes
from Cuentas import views as views_Cuentas
from Prestamos import views as views_Prestamos
from Tarjetas import views as views_Tarjetas

urlpatterns = [
    path('', views_Base.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro', views_Base.registro, name="registro"),
    path('admin/', admin.site.urls),    
    path('clientes/', views_Clientes.clientes, name="clientes"),
    path('cuentas/', views_Cuentas.cuentas, name="cuentas"),
    path('prestamos/', views_Prestamos.prestamos, name="prestamos"),
    path('tarjetas/', views_Tarjetas.tarjetas, name="tarjetas"),
]
