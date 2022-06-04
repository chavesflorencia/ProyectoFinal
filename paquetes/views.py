from django.shortcuts import render
from paquetes.models import paquete, cliente, user, compra
# Create your views here.
def paquetes(request):
    paquetes = paquete.objects.all()
    print(paquetes)
    context = {'paquetes': paquetes}
    return render(request, "template_1.html", context = context) 

def clientes(request):
    clientes = cliente.objects.all()
    print(clientes)
    context = {'clientes': clientes}
    return render(request, "template_2.html", context = context) 

def usuarios(request):
    usuarios = user.objects.all()
    print(usuarios)
    context = {'usuarios': usuarios}
    return render(request, "template_3.html", context = context) 

def transacciones(request):
    transacciones = compra.objects.all()
    print(transacciones)
    context = {'transacciones': transacciones}
    return render(request, "template_4.html", context = context) 