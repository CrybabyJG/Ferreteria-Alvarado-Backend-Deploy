from django.urls import path
from .views import ClientesAPIView

app_name = 'Clientes'

urlpatterns = [
    path('', ClientesAPIView.as_view(), name="clientes")
]