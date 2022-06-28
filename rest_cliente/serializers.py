from dataclasses import field, fields
from msilib.schema import ServiceInstall
from rest_framework import serializers
from core.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields =['id_cliente','nombre','apellidos','correo','direccion']