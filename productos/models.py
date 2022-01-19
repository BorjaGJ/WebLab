from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    CAS = models.CharField(max_length=50, blank=True)
    codigo_laboratorio = models.CharField(max_length=100)
    organico = models.BooleanField(default=False)
    cantidad = models.CharField(max_length=50)
    ficha_seguridad = models.FileField(null=True, blank=True)
    ubicacion = RichTextUploadingField()


    class Meta:
        abstract = True

    def __str__(self):
        return u"%s" % self.nombre



class Patron(Producto):
    matriz = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=100)
    certificado = models.FileField(null=True, blank=True)


class Reactivo(Producto):
    pureza = models.DecimalField(max_digits=3, decimal_places=3)


class Disolvente(Producto):
    densidad = models.CharField(max_length=50)