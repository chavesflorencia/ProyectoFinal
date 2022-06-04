from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_pasaporte(value):
    if value(len) != 8:
        raise ValidationError(
            _('%(value)s is not a valid passport/dni number'),
            params={'value': value},
        )

def validate_telefono(value):
    if value(len) != 8:
        raise ValidationError(
            _('%(value)s is not a valid telephone number'),
            params={'value': value},
        )

# Create your models here.
class paquete(models.Model):
    destino = models.CharField(max_length=30)    
    descripcion = models.CharField(max_length=30)   
    dias = models.DateField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    precio_publico = models.FloatField()
    costo = models.FloatField()
    activo = models.BooleanField()

class cliente(models.Model):
    id_user = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pasaporte = models.IntegerField(validators=[validate_pasaporte])
    vencimiento = models.DateField()
    dni = models.IntegerField(validators=[validate_pasaporte])
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField(validators=[validate_telefono])

class user(models.Model):
    USER_TYPES = (
        ('SU', 'Super_user'),
        ('RU', 'Regular_user'),
    )
    usertype = models.CharField(max_length=2, choices= USER_TYPES)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    last_login = models.DateField()
    activo = models.BooleanField()

class compra(models.Model):
    paquete = models.CharField(max_length=30)
    cantidad_pasajeros = models.IntegerField()
    dias = models.IntegerField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    fecha_venta = models.DateField(auto_now = True)
    PAYMENT_TYPES = (
        ('Tr', 'Transferencia bancaria'),
        ('TC', 'Tarjeta de credito'),
        ('TD', 'Tarjeta de debito'),
        ('MP', 'Mercado Pago'),
    )
    forma_pago = models.CharField(max_length=2, choices=PAYMENT_TYPES)
    activo = models.BooleanField()

