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


class Trabajador(Persona):
    fecha_incorporacion = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=100)
    password_confirm = models.CharField(max_length=100)
    personal = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #
    #     user = get_object_or_None(User, username=self.nombre)
    #
    #
    #     if user is None:
    #
    #         user = User.objects.create(
    #             username=self.nombre,
    #             email=self.email,
    #             password=self.password,
    #             is_staff=self.personal,
    #             is_superuser=self.admin,
    #             is_active=True,
    #         )
    #         user.save()
    #         self.usuario = user
    #
    #
    #     else:
    #         user.username = self.nombre
    #         user.email = self.email
    #         user.password = self.password
    #         user.is_staff = self.personal
    #         user.is_superuser = self.admin
    #         user.save()
    #
    #
    #
    #     super(Trabajador, self).save(*args, **kwargs)




class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    fecha_espera = models.DateField(blank=True, null=True)
    fecha_recibido = models.DateField(blank=True, null=True)
    albaran = models.FileField(blank=True, null=True, upload_to='albaran')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=10)

    def __str__(self):
        return self.nombre + " de " + self.proveedor.nombre


    def save(self, *args, **kwargs):
        proveedor = Proveedor.objects.get(nombre=self.proveedor.nombre)
        pedidos = Pedido.objects.filter(proveedor=self.proveedor)

        proveedor.nota = pedidos.aggregate(Avg('puntuacion'))['puntuacion__avg']
        print(proveedor.nota)
        proveedor.save()

        super(Pedido, self).save(*args, **kwargs)


class Analisis(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_expiracion = models.DateField(null=True, blank=True, editable=False)
    fecha_terminado = models.DateField(null=True, blank=True)
    resultado = models.FileField(blank=True, null=True, upload_to='resultados')
    factura = models.FileField(blank=True, null=True, upload_to='facturas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.cliente.nombre

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










