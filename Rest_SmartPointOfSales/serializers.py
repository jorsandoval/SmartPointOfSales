from dataclasses import field
from rest_framework import serializers
from core.models import Cliente

class ClienteSerualizer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        field =['id_cliente','nombre','apellidos','correo','direccion']