from django.db.models import Q
from django.shortcuts import redirect, render

from material.forms import VolumetricoForm
from material.models import Volumetrico
from web import views

class VolumetricosView(views.TableView):
    template_name = 'volumetricos.html'
    model = Volumetrico


class VolumetricoEditView(views.EditView):
    template_name = 'edit_volumetrico.html'
    model = Volumetrico
    model_form = VolumetricoForm
    redirect_to = 'volumetrico'


class VolumetricoAddView(views.AddView):
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