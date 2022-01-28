from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class PoliticaPrivacidad(models.Model):
    texto = RichTextUploadingField()
    archivo = models.FileField(blank=True, null=True)


class Condiciones(PoliticaPrivacidad):
    pass
