from dataclasses import field, fields
from msilib.schema import ServiceInstall
from rest_framework import serializers
from core.models import Cliente, Producto, Venta, DetalleVenta, MedioPago

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields =['id_cliente','nombre','apellidos','correo','direccion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =['id_venta','monto','medioPago','fecha','cliente']

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']

class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nombre']
