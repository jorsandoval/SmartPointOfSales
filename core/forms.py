from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Cliente, Venta, DetalleVenta, MedioPago, Producto

#Creamos nuestra clase para el formulario desde la base de datos
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['id_cliente','nombre','apellidos','correo','direccion']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields =['id_venta','monto','medioPago','fecha','cliente']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio']

class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']

class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nombre']


