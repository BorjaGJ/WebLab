from annoying.functions import get_object_or_None
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from web import views

from productos.forms import ReactivoForm, DisolventeForm
from productos.models import Reactivo, Disolvente, Patron


class ReactivoTableView(views.TableView):
    pass


class ReactivoEditView(views.EditView):
    pass

class ReactivoAddView(views.AddView):
    pass


def DeleteReactivo(request, **kwargs):

    model = Reactivo
    redirect_to = 'reactivos'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


def searchReactivo(request):

    model = Reactivo

    if request.method == 'GET':

        buscado = request.GET.get('buscarReactivo')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(CAS__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'reactivos.html', {"entradas": entradas})

    else:
        entradas = model.objects.all()
        return render(request, "reactivos.html", {"entradas": entradas})


class DisolventeView(views.TableView):
    template_name = 'disolventes.html'
    model = Disolvente


class DisolventeAddView(views.AddView):
    template_name = 'add_disolvente.html'
    model = Disolvente
    redirect_to = 'disolventes'
    model_form = DisolventeForm

class DisolventeEditView(views.EditView):
    template_name = 'disolvente_edit.html'
    model = Disolvente
    model_form = DisolventeForm
    redirect_to = 'disolventes'

def DeleteDisolvente(request, **kwargs):

    model = Disolvente
    redirect_to = 'disolventes'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)


class PatronesView(views.TableView):
    template_name = 'patrones.html'
    model = Patron

