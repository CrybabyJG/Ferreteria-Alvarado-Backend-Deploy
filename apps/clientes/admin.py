from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.clientes.models import Clientes
# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(ModelAdmin):
    search_fields = ['Nombres', 'Telefono', 'Correo', 'Fecha_Registro', 'Origen']
    list_display = ['Nombres', 'Telefono', 'Correo', 'Fecha_Registro', 'Origen', 'Interes']