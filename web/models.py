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
        from productos.models import Disolvente
        from productos.models import Reactivo
        from productos.models import Patron

        if modelEventoColorHasChanged(Instrumento, self.color_instrumentos):
            instrumentos = Instrumento.objects.all()
            for reactivo in instrumentos:
                reactivo.evento.color = self.color_instrumentos
                reactivo.save()

        if modelEventoColorHasChanged(Volumetrico, self.color_volumetricos):
            volumetricos = Volumetrico.objects.all()
            for patron in volumetricos:
                patron.evento.color = self.color_volumetricos
                patron.save()

        if modelEventoColorHasChanged(Miscelanea, self.color_miscelaneas):
            miscelaneas = Miscelanea.objects.all()
            for disolvente in miscelaneas:
                disolvente.evento.color = self.color_miscelaneas
                disolvente.save()

        if modelEventoColorHasChanged(Reactivo, self.color_reactivos):
            reactivos = Reactivo.objects.all()
            for reactivo in reactivos:
                reactivo.evento.color = self.color_reactivos
                reactivo.save()

        if modelEventoColorHasChanged(Patron, self.color_patrones):
            patrones = Patron.objects.all()
            for patron in patrones:
                patron.evento.color = self.color_patrones
                patron.save()

        if modelEventoColorHasChanged(Disolvente, self.color_miscelaneas):
            disolventes = Disolvente.objects.all()
            for disolvente in disolventes:
                disolvente.evento.color = self.color_disolventes
                disolvente.save()


def modelEventoColorHasChanged(Model, color_configuracion):
    entrada = Model.objects.first()
    devolver = False

    if entrada is None:
        devolver = False

    else:
        devolver = entrada.evento.color != color_configuracion

    return devolver


