from annoying.functions import get_object_or_None
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.contrib.auth.models import User
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
        from otros.models import Analisis
        from otros.models import Pedido

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

        if modelEventoColorHasChanged(Analisis, self.color_analisis):
            analisis = Analisis.objects.all()
            for analisis in analisis:
                analisis.evento.color = self.color_analisis
                analisis.save()

        if modelEventoColorHasChanged(Pedido, self.color_analisis):
            pedidos = Pedido.objects.all()
            for pedido in pedidos:
                pedido.evento.color = self.color_pedidos
                pedido.save()



def modelEventoColorHasChanged(Model, color_configuracion):

    entrada = Model.objects.last()

    if entrada is None:
        devolver = False

    else:
        devolver = entrada.evento.color != color_configuracion

    print(devolver)

    return devolver


class CustomPermisos(models.Model):
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_color = models.BooleanField(default=False)
    can_user = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username


