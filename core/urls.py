from django.urls import path
from .views import form_mod_producto, home, home_cliente, home_detalle_venta, home_medio_pago, home_producto, home_venta, form_cliente, form_venta, form_producto, form_medio_pago, form_detalle_venta, form_mod_cliente, form_mod_producto, form_mod_medio_pago, form_mod_venta


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
    path('form_detalle_venta', form_detalle_venta, name="form_detalle_venta"),
    path('form_medio_pago', form_medio_pago, name="form_medio_pago"),
    path('form_mod_cliente/<id_cliente>', form_mod_cliente, name="form_mod_cliente"),
    path('form_mod_producto/<id_producto>', form_mod_producto, name="form_mod_producto"),
    path('form_mod_medio_pago/<id_medio_pago>', form_mod_medio_pago, name="form_mod_medio_pago"),
    path('form_mod_venta/<id_venta>', form_mod_venta, name="form_mod_venta"),
]