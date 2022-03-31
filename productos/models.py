from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from material.models import no_space_validator, no_asciis_validator
from otros.models import Proveedor


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_slug = models.SlugField(blank=True, editable=False)
    CAS = models.CharField(max_length=50)
    codigo_laboratorio = models.CharField(unique=True, max_length=100, validators=[no_space_validator, no_asciis_validator])
    organico = models.BooleanField(default=False)
    cantidad = models.CharField(max_length=50)
    ubicacion = RichTextUploadingField(default='En el laboratorio', blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    fecha_caducidad = models.DateField()
    ficha_seguridad = models.FileField(blank=True, null=True)


    class Meta:
        abstract = True

    def __str__(self):
        return u"%s" % self.nombre


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)



class Patron(Producto):
    matriz = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=100)
    certificado = models.FileField(blank=True, null=True)


class Reactivo(Producto):
    pureza = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=5, decimal_places=2)


class Disolvente(Producto):
    densidad = models.CharField(max_length=50)