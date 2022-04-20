from django.db.models import Q
from django.shortcuts import redirect, render

from material.forms import VolumetricoForm, InstrumentoForm, MiscelaneaForm
from material.models import Volumetrico, Instrumento, Miscelanea
from web import views_utils


class VolumetricosView(views_utils.TableView):
    template_name = 'volumetricos.html'
    model = Volumetrico


class DetalleVolumetricoView(views_utils.DetalleView):
    template_name = 'detail_volumetrico.html'
    model = Volumetrico


class VolumetricoEditView(views_utils.EditView):
    template_name = 'edit_volumetrico.html'
    model = Volumetrico
    model_form = VolumetricoForm
    redirect_to = 'volumetrico'


class VolumetricoAddView(views_utils.AddView):
    template_name = 'add_volumetrico.html'
    model = Volumetrico
    model_form = VolumetricoForm
    redirect_to = 'volumetrico'

def deleteVolumetrico(request, **kwargs):

    model = Volumetrico
    redirect_to = 'volumetrico'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def searchVolumetrico(request):

    model = Volumetrico

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'volumetricos.html', {"entradas": entradas})


class InstrumentosView(views_utils.TableView):
    template_name = 'instrumentos.html'
    model = Instrumento


class DetalleInstrumentoView(views_utils.DetalleView):
    template_name = 'detail_instrumento.html'
    model = Instrumento


class InstrumentoEditView(views_utils.EditView):
    template_name = 'edit_instrumento.html'
    model = Instrumento
    model_form = InstrumentoForm
    redirect_to = 'instrumento'


class InstrumentoAddView(views_utils.AddView):
    template_name = 'add_instrumento.html'
    model = Instrumento
    model_form = InstrumentoForm
    redirect_to = 'instrumento'

def deleteInstrumento(request, **kwargs):

    model = Instrumento
    redirect_to = 'instrumento'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def searchInstrumento(request):

    model = Instrumento

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'instrumentos.html', {"entradas": entradas})


class MiscelaneasView(views_utils.TableView):
    template_name = 'micelaneas.html'
    model = Miscelanea


class DetalleMiscelaneaView(views_utils.DetalleView):
    template_name = 'detail_miscelanea.html'
    model = Miscelanea


class MiscelaneaEditView(views_utils.EditView):
    template_name = 'edit_miscelanea.html'
    model = Miscelanea
    model_form = MiscelaneaForm
    redirect_to = 'miscelanea'


class MiscelaneaAddView(views_utils.AddView):
    template_name = 'add_miscelanea.html'
    model = Miscelanea
    model_form = MiscelaneaForm
    redirect_to = 'miscelanea'


def deleteMiscelanea(request, **kwargs):

    model = Miscelanea
    redirect_to = 'miscelanea'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def searchMiscelanea(request):

    model = Miscelanea

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado)  |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'instrumentos.html', {"entradas": entradas})