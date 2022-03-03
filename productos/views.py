from django.db.models import Q
from django.shortcuts import render, redirect
from web import views_utils

from productos.forms import DisolventeForm, PatronForm
from productos.models import Reactivo, Disolvente, Patron


# Vistas de reactivos

class ReactivoTableView(views_utils.TableView):
    pass


class ReactivoEditView(views_utils.EditView):
    pass

class ReactivoAddView(views_utils.AddView):
    pass


def deleteReactivo(request, **kwargs):

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


#Vistas de disolventes

class DisolventeView(views_utils.TableView):
    template_name = 'disolventes.html'
    model = Disolvente


class DisolventeAddView(views_utils.AddView):
    template_name = 'add_disolvente.html'
    model = Disolvente
    redirect_to = 'disolventes'
    model_form = DisolventeForm

class DisolventeEditView(views_utils.EditView):
    template_name = 'edit_disolvente.html'
    model = Disolvente
    model_form = DisolventeForm
    redirect_to = 'disolventes'

def deleteDisolvente(request, **kwargs):

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



# Vistas de patrones

class PatronesView(views_utils.TableView):
    template_name = 'patrones.html'
    model = Patron

class PatronAddView(views_utils.AddView):
    template_name = 'add_patron.html'
    model = Patron
    model_form = PatronForm
    redirect_to = 'patrones'

class PatronEditView(views_utils.EditView):
    template_name = 'edit_patron.html'
    model = Patron
    model_form = PatronForm
    redirect_to = 'patrones'


def deletePatron(request, **kwargs):

    model = Disolvente
    redirect_to = 'patron'

    entrada = model.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect(redirect_to)

def searchPatron(request):

    model = Patron

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(CAS__icontains=buscado) |
            Q(codigo_laboratorio__icontains=buscado) | Q(proveedor__nombre__icontains=buscado)
        )
        return render(request, 'patrones.html', {"entradas": entradas})
