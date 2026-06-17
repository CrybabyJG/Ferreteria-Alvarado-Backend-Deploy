from django.urls import path, include

urlpatterns = [
    path('clientes/', include('apps.clientes.urls'))
]