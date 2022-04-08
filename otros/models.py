from datetime import datetime
from datetime import timedelta
from annoying.functions import get_object_or_None
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify

from web.models import ConfiguracionEventos


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
            eventos = Evento.objects.filter(fecha__month=hoy.month, fecha__year=hoy.year)
            for evento in eventos:
                lista_eventos.append(evento.fecha.day)

        except Evento.DoesNotExist:
            pass

        return lista_eventos

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_slug = models.SlugField(unique=True, blank=True, editable=False)
    nota = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True, editable=False, default=0)
    pagina_web = models.URLField(null=True, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Proveedor, self).save(*args, **kwargs)



class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_slug = models.SlugField(unique=True, editable=False, blank=True, null=True)
    dni = models.CharField(validators=[RegexValidator(r'^[0-9]{8,8}[A-Za-z]$', 'DNI  introducido no valido')],
                           max_length=9)
    cp = models.CharField(max_length=10)
    poblacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Persona, self).save(*args, **kwargs)


class Cliente(Persona):
    pass


class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_espera = models.DateField()
    fecha_recibido = models.DateField(blank=True, null=True)
    albaran = models.FileField(blank=True, null=True, upload_to='albaran')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    puntuacion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=10)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre + " de " + self.proveedor.nombre


    def save(self, *args, **kwargs):
        proveedor = Proveedor.objects.get(nombre=self.proveedor.nombre)
        pedidos = Pedido.objects.filter(proveedor=self.proveedor)

        proveedor.nota = pedidos.aggregate(Avg('puntuacion'))['puntuacion__avg']
        print(proveedor.nota)
        proveedor.save()
        evento = self.evento

        configuracion = ConfiguracionEventos.objects.all().last()

        if configuracion is None:
            configuracion = ConfiguracionEventos.objects.create()

        if evento is None:
            evento = Evento.objects.create(
                nombre='LLega pedido ' + self.nombre, fecha=self.fecha_espera, color=configuracion.color_pedidos
            )
            self.evento = evento


        else:
            evento.fecha = self.fecha_espera
            evento.nombre = self.nombre
            evento.color = configuracion.color_pedidos
            evento.save()

        super(Pedido, self).save(*args, **kwargs)


class Analisis(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_expiracion = models.DateField()
    fecha_terminado = models.DateField(null=True, blank=True)
    resultado = models.FileField(blank=True, null=True, upload_to='resultados')
    factura = models.FileField(blank=True, null=True, upload_to='facturas')
    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):

            evento = self.evento

            configuracion = ConfiguracionEventos.objects.all().last()

            if configuracion is None:
                configuracion = ConfiguracionEventos.objects.create()

            if evento is None:
                evento = Evento.objects.create(
                    nombre='Expiración analisis' + self.nombre, fecha=self.fecha_expiracion,
                    color=configuracion.color_analisis
                )
                self.evento = evento


            else:
                evento.fecha = self.fecha_expiracion
                evento.nombre = self.nombre
                evento.color = configuracion.color_analisis
                evento.save()

            super(Analisis, self).save(*args, **kwargs)













