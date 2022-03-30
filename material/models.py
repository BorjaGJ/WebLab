from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from annoying.functions import get_object_or_None

from otros.models import Proveedor, Evento

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
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    ubicacion = RichTextUploadingField(default='En el laboratiorio')
    proxima_revision = models.DateField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, editable=False, null=True, blank=True)


    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        evento = self.evento

        if evento is None:
            evento = Evento.objects.create(nombre=self.nombre, fecha=self.proxima_revision)
            self.evento = evento
            evento.save()

        else:
            evento.fecha = self.proxima_revision
            evento.nombre = self.nombre
            evento.save()

        super(Material, self).save(*args, **kwargs)




class Volumetrico(Material):
    OPTION_CHOICES = (("Aforado", "Aforado"), ("Graduado", "Graduado"))
    graduacion = models.CharField(choices=OPTION_CHOICES, max_length=10)
    volumen = models.CharField(max_length=20)
    cuantia = models.IntegerField(validators=[MinValueValidator(0)])


class Instrumento(Material):
    metodo_calibracion = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Miscelanea(Material):
    pass
