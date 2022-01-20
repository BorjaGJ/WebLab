from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from evaluables.models import Proveedor


class Material(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = RichTextUploadingField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Volumetrico(Material):
    OPTION_CHOICES = (("Aforado", "Aforado"), ("Graduado", "Graduado"))
    Graduacion = models.CharField(choices=OPTION_CHOICES, max_length=10)
    lote = models.CharField(max_length=20, blank=True, null=True)
    volumen = models.CharField(max_length=20)


class Miscelania(Material):
    pass


