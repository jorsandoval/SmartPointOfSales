from django.urls import path
from .views import home, home_cliente

URLPattern = [
    path('', home, name="home"),
    path('home_cliente', home_cliente, name="home_cliente"),
    #path('form_cliente',form_cliente, name="form_cliente"),
    #path('form_venta',form_venta, name="form_venta"),
    #path('form_producto',form_producto, name="form_producto"),
]