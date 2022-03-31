from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db import models


class PoliticaPrivacidad(models.Model):
    texto = RichTextUploadingField()
    archivo = models.FileField(blank=True, null=True)


class Condiciones(PoliticaPrivacidad):
    pass


class ConfiguracionEventos(models.Model):
    color_instrumentos = ColorField(default='#0d6efd')
    color_volumetricos = ColorField(default='#0d6efd')
    color_miscelaneas = ColorField(default='#0d6efd')
    color_patrones = ColorField(default='#0d6efd')
    color_reactivos = ColorField(default='#0d6efd')
    color_disolventes = ColorField(default='#0d6efd')
    color_pedidos = ColorField(default='#0d6efd')
    color_analisis = ColorField(default='#0d6efd')

