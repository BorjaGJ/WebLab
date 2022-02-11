from datetime import datetime

from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from regex_field.fields import RegexField




class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nota = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(10)], decimal_places=2, max_digits=4)
    pagina_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(validators=[RegexValidator(r'^[0-9]{8,8}[A-Za-z]$', 'DNI  introducido no valido')],
                           max_length=9)
    cp = models.CharField(max_length=10)
    poblacion = models.CharField(max_length=50)
    telefono = RegexField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Telefono introducido no valido')],
                          max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Cliente(Persona):
    pass


class Trabajador(Persona):
    fecha_incorporacion = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class Pedido(models.Model):
    fecha_pedido = models.DateField()
    fecha_recibido = models.DateField(auto_now_add=True, blank=True, null=True)
    albaran = models.FileField(blank=True, null=True)
    contenido = RichTextUploadingField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.fecha_pedido.__str__() + self.proveedor.nombre


class Analisis(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_pedido = models.DateField(auto_now_add=True)
    resguardo = models.FileField(blank=True, null=True)
    resultado = models.FileField(blank=True, null=True)
    factura = models.FileField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + self.cliente.nombre



class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    color = ColorField(default='#0d6efd')

    @property
    def get_dias_eventos_instrumentos(self):

        hoy = datetime.now()
        lista_eventos = []

        try:
            from material.models import Instrumento
            instrumentos = Instrumento.objects.filter(proxima_revision__month=hoy.month)

            for instrumento in instrumentos:
                lista_eventos.append(instrumento.proxima_revision.day)

        except Evento.DoesNotExist:
             pass

        return lista_eventos

    @property
    def get_dias_eventos(self):

        hoy = datetime.now()
        lista_eventos = []
        try:
            eventos = Evento.objects.filter(fecha__month=hoy.month)
            for evento in eventos:
                lista_eventos.append(evento.fecha.day)

        except Evento.DoesNotExist:
            pass

        return lista_eventos

    def __str__(self):
        return self.nombre










