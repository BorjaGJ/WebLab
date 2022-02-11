from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from otros.models import Proveedor

no_space_validator = RegexValidator(
    r' ',
    'No se permiten espacios',
    inverse_match=True,
    code='invalid_tag',
)

class Material(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_laboratorio = models.CharField(unique=True, max_length=100, validators=[no_space_validator])
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    ubicacion = RichTextUploadingField(default='En el laboratiorio')


    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Volumetrico(Material):
    OPTION_CHOICES = (("Aforado", "Aforado"), ("Graduado", "Graduado"))
    graduacion = models.CharField(choices=OPTION_CHOICES, max_length=10)
    lote = models.CharField(max_length=20, blank=True, null=True)
    volumen = models.CharField(max_length=20)
    cuantia = models.IntegerField(validators=[MinValueValidator(0)])


class Instrumento(Material):
    manual = models.FileField(blank=True, null=True)
    metodo_calibracion = models.FileField(blank=True, null=True)
    proxima_revision = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Miscelanea(Material):
    pass
