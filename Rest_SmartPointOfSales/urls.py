from django.urls import path
from Rest_SmartPointOfSales.views import lista_clientes, lista_productos, lista_ventas, lista_detalle_venta, lista_medio_pago

urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('lista_productos', lista_productos, name="lista_productos"),
    path('lista_ventas', lista_ventas, name="lista_ventas"),
    path('lista_detalle_venta', lista_detalle_venta, name="lista_detalle_venta"),
    path('lista_medio_pago', lista_medio_pago, name="lista_medio_pago"),
]
