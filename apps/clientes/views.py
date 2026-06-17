from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clientes.models import Clientes
from apps.clientes.serializer import ClientesSerializer


# Create your views here.
class ClientesAPIView(APIView):
    model = Clientes

    def get(self, request):
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)