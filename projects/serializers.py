from rest_framework import serializers
from .models import Productor

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields = ('id', 'nombre', 'apellidos', 'DNI', 'email', 'telefono', 'fecha_registro', 'estado')
        read_only_fields = ('fecha_registro',)
