from django.shortcuts import render
from paquetes.models import paquete, cliente, user, compra
# Create your views here.
def paquetes(request):
    paquetes = paquete.objects.all()
    print(paquetes)
    context = {'paquetes': paquetes}
    return render(request, "template_1.html", context = context) 