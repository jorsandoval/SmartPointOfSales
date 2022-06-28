from django.urls import path
from rest_venta.views import lista_ventas, lista_detalle_venta, lista_medio_pago

urlpatterns = [
    path('lista_ventas', lista_ventas, name="lista_ventas"),
    path('lista_detalle_venta', lista_detalle_venta, name="lista_detalle_venta"),
    path('lista_medio_pago', lista_medio_pago, name="lista_medio_pago"),
]
