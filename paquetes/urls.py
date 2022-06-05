from django.urls import path
from paquetes.views import paquetes, clientes, usuarios, transacciones

urlpatterns = [
    path('', paquetes, name = 'paquetes'),
    path('clientes/', clientes, name = 'clientes'),
    path('usuarios/', usuarios, name = 'usuarios'),
    path('transacciones/', transacciones, name = 'transacciones')
]
