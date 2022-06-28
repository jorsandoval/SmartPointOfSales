from dataclasses import field, fields
from msilib.schema import ServiceInstall
from rest_framework import serializers
from core.models import  Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio']