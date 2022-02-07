from django.db.models import Q
from django.shortcuts import redirect, render

from material.forms import VolumetricoForm, InstrumentoForm
from material.models import Volumetrico, Instrumento
from web import views_utils

class VolumetricosView(views_utils.TableView):
    template_name = 'volumetricos.html'
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

def DeleteVolumetrico(request, **kwargs):

    model = Volumetrico
    redirect_to = 'volumetrico'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def SearchVolumetrico(request):

    model = Volumetrico

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(lote__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'volumetricos.html', {"entradas": entradas})



class InstrumentosView(views_utils.TableView):
    template_name = 'instrumentos.html'
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

def DeleteInstrumento(request, **kwargs):

    model = Instrumento
    redirect_to = 'instrumento'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def SearchInstrumento(request):

    model = Instrumento

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(lote__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'instrumentos.html', {"entradas": entradas})