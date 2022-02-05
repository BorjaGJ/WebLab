from django.db.models import Q
from django.shortcuts import render, redirect
from web import views

from productos.forms import ReactivoForm, DisolventeForm, PatronForm
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


class DisolventeView(views.TableView):
    template_name = 'disolventes.html'
    model = Disolvente


class DisolventeAddView(views.AddView):
    template_name = 'add_disolvente.html'
    model = Disolvente
    redirect_to = 'disolventes'
    model_form = DisolventeForm

class DisolventeEditView(views.EditView):
    template_name = 'edit_disolvente.html'
    model = Disolvente
    model_form = DisolventeForm
    redirect_to = 'disolventes'

def DeleteDisolvente(request, **kwargs):

    model = Disolvente
    redirect_to = 'disolventes'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)

def searchDisolvente(request):

    model = Disolvente

    if request.method == 'GET':

        buscado = request.GET.get('buscarDisolvente')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(CAS__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'disolventes.html', {"entradas": entradas})


class PatronesView(views.TableView):
    template_name = 'patrones.html'
    model = Patron

class PatronAddView(views.AddView):
    template_name = 'add_patron.html'
    model = Patron
    model_form = PatronForm
    redirect_to = 'patrones'

class PatronEditView(views.EditView):
    template_name = 'edit_patron.html'
    model = Patron
    model_form = PatronForm
    redirect_to = 'patrones'

def DeletePatron(request, **kwargs):

    model = Patron
    redirect_to = 'patrones'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)

def searchPatron(request):

    model = Patron

    if request.method == 'GET':

        buscado = request.GET.get('buscarPatron')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(CAS__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'patrones.html', {"entradas": entradas})
