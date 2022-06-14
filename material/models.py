from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from annoying.functions import get_object_or_None
from django.template.defaultfilters import slugify

from otros.models import Proveedor, Evento
from web.models import ConfiguracionEventos

no_space_validator = RegexValidator(
    r' ',
    'No se permiten espacios',
    inverse_match=True,
    code='invalid_tag',
)
no_asciis_validator = RegexValidator(
    r'[^\w|^\s]+',
    'Carácter no válido',
    inverse_match=True,
    code='invalid_character'
)
class Material(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_laboratorio = models.CharField(unique=True, max_length=100, validators=[no_space_validator, no_asciis_validator])
    codigo_slug = models.CharField(max_length=100, blank=True, null=True, editable=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, blank=True, null=True)
    ubicacion = RichTextUploadingField(default='En el laboratorio')
    proxima_revision = models.DateField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, editable=False, null=True, blank=True)


    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre




class Volumetrico(Material):
    OPTION_CHOICES = (("Aforado", "Aforado"), ("Graduado", "Graduado"), ("Ninguna", "Ninguna"))
    graduacion = models.CharField(choices=OPTION_CHOICES, max_length=10)
    volumen = models.CharField(max_length=20)
    cuantia = models.IntegerField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):

        evento = self.evento

        configuracion = ConfiguracionEventos.objects.all().last()

        if configuracion is None:
            configuracion = ConfiguracionEventos.objects.create()

        if evento is None:
            evento = Evento.objects.create(
                nombre='Revisión de '+self.nombre, fecha=self.proxima_revision, color=configuracion.color_volumetricos
            )
            self.evento = evento


        else:
            evento.fecha = self.proxima_revision
            evento.nombre = self.nombre
            evento.color = configuracion.color_volumetricos
            evento.save()


        self.codigo_slug = slugify(self.codigo_laboratorio)

        super(Volumetrico, self).save(*args, **kwargs)


class Instrumento(Material):
    metodo_calibracion = models.FileField(upload_to='metodos', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        evento = self.evento

        configuracion = ConfiguracionEventos.objects.all().last()

        if configuracion is None:
            configuracion = ConfiguracionEventos.objects.create()


        if evento is None:
            evento = Evento.objects.create(
                nombre='Revision de ' + self.nombre, fecha=self.proxima_revision, color=configuracion.color_instrumentos
            )
            self.evento = evento


        else:
            evento.fecha = self.proxima_revision
            evento.nombre = self.nombre
            evento.color = configuracion.color_instrumentos
            evento.save()

        self.codigo_slug = slugify(self.codigo_laboratorio)

        super(Instrumento, self).save(*args, **kwargs)


class Miscelanea(Material):

    def save(self, *args, **kwargs):

        evento = self.evento

        configuracion = ConfiguracionEventos.objects.all().last()

        if configuracion is None:
            configuracion = ConfiguracionEventos.objects.create()

        if evento is None:
            evento = Evento.objects.create(
                nombre='Revisión de ' + self.nombre, fecha=self.proxima_revision, color=configuracion.color_miscelaneas
            )
            self.evento = evento


        else:
            evento.fecha = self.proxima_revision
            evento.nombre = self.nombre
            evento.color = configuracion.color_miscelaneas
            evento.save()

        self.codigo_slug = slugify(self.codigo_laboratorio)

        super(Miscelanea, self).save(*args, **kwargs)
