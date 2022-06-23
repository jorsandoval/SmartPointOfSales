"""SmartPointOfSales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core.views import home_cliente, form_cliente, form_venta,form_producto,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('home-cliente', home_cliente, name="home_cliente"),
    path('form-cliente',form_cliente, name="form_cliente"),
    path('form-venta',form_venta, name="form_venta"),
    path('form-producto',form_producto, name="form_producto"),
]
