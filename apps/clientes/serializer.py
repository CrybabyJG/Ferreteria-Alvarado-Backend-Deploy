from rest_framework import serializers

from apps.clientes.models import Clientes
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'