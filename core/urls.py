from django.urls import path
from .views import home, home_cliente, home_detalle_venta, home_medio_pago, home_producto, home_venta, form_cliente, form_venta, form_producto, form_mediopago


urlpatterns = [
    path('', home, name="home"),
    path('home_cliente', home_cliente, name="home_cliente"),
    path('home_detalle_venta', home_detalle_venta, name="home_detalle_venta"),
    path('home_medio_pago', home_medio_pago, name="home_medio_pago"),
    path('home_producto', home_producto, name="home_producto"),
    path('home_venta', home_venta, name="home_venta"),
    path('form_cliente',form_cliente, name="form_cliente"),
    path('form_venta',form_venta, name="form_venta"),
    path('form_producto',form_producto, name="form_producto"),
    path('form_mediopago', form_mediopago, name="form_mediopago"),
]