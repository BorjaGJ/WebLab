from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models

from evaluables.models import Proveedor


class Material(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_laboratorio = models.CharField(unique=True, max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    ubicacion = RichTextUploadingField(default='En el laboratiorio')
    proxima_revision = models.DateField(blank=True, null=True)

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


class Miscelania(Material):
    pass


class Intrumento(Material):
    manual = models.FileField(blank=True, null=True)
    certificado_de_calibracion = models.FileField(blank=True, null=True)
    metodo_calibracion = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nombre
