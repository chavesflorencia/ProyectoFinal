from django.contrib import admin
from paquetes.models import paquete, cliente, user, compra
# Register your models here.

admin.site.register(paquete)
admin.site.register(cliente)
admin.site.register(user)
admin.site.register(compra)
