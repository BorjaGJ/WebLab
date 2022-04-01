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

    def save(self, *args, **kwargs):
        super(ConfiguracionEventos, self).save(*args, **kwargs)

        from material.models import Instrumento
        from material.models import Volumetrico
        from material.models import Miscelanea

        if modelEventoColorHasChanged(Instrumento, self.color_instrumentos):
            instrumentos = Instrumento.objects.all()
            for instrumento in instrumentos:
                instrumento.evento.color = self.color_instrumentos
                instrumento.save()

        if modelEventoColorHasChanged(Volumetrico, self.color_volumetricos):
            volumetricos = Volumetrico.objects.all()
            for volumetrico in volumetricos:
                volumetrico.evento.color = self.color_volumetricos
                volumetrico.save()

        if modelEventoColorHasChanged(Miscelanea, self.color_miscelaneas):
            miscelaneas = Miscelanea.objects.all()
            for miscelanea in miscelaneas:
                miscelanea.evento.color = self.color_miscelaneas
                miscelanea.save()


def modelEventoColorHasChanged(Model, color_configuracion):
    entrada = Model.objects.first()
    configuracion = ConfiguracionEventos.objects.all().last()

    return entrada.evento.color != color_configuracion


