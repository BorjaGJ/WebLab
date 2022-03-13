import datetime

from django.db.models import Q
from django.shortcuts import redirect, render

from otros.forms import EventoForm, ClienteForm, ProveedorForm
from otros.models import Evento, Cliente, Proveedor
from web.views_utils import TableView, EditByIdView, AddView


class EventosTableView(TableView):
    model = Evento
    template_name = 'eventos.html'
    order_by = 'fecha'


class EventoEditView(EditByIdView):
    model = Evento
    redirect_to = 'eventos'
    model_form = EventoForm
    template_name = 'edit_evento.html'


class EventoAddView(AddView):
    model = Evento
    redirect_to = 'eventos'
    model_form = EventoForm
    template_name = 'add_evento.html'




def deleteEvento(request, **kwargs):

    model = Evento
    redirect_to = 'eventos'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchEvento(request):

    model = Evento

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado))
        return render(request, 'clientes.html', {"entradas": entradas})


def delete_expired(request):
    hoy = datetime.datetime.now().date()
    eventos = Evento.objects.all()

    for evento in eventos:
        if evento.fecha < hoy:
            evento.delete()

    return redirect('eventos')

class ClienteTableView(TableView):
    model = Cliente
    template_name = 'clientes.html'
    order_by = 'nombre'

class ClienteAddView(AddView):
    model = Cliente
    redirect_to = 'clientes'
    model_form = ClienteForm
    template_name = 'add_cliente.html'

class ClienteEditView(EditByIdView):
    model = Cliente
    redirect_to = 'clientes'
    model_form = ClienteForm
    template_name = 'edit_cliente.html'

def deleteCliente(request, **kwargs):

    model = Cliente
    redirect_to = 'clientes'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchCliente(request):

    model = Cliente

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(dni__icontains=buscado) |
            Q(telefono__icontains=buscado) | Q(email__icontains=buscado) |
            Q(cp__icontains=buscado) | Q(poblacion__icontains=buscado)
        )

        return render(request, 'clientes.html', {"entradas": entradas})


class ProveedoresTableView(TableView):
    model = Proveedor
    template_name = 'proveedores.html'
    order_by = 'id'


class ProveedoresEditView(EditByIdView):
    model = Proveedor
    redirect_to = 'proveedores'
    model_form = ProveedorForm
    template_name = 'edit_proveedor.html'


class ProveedoresAddView(AddView):
    model = Proveedor
    redirect_to = 'proveedores'
    model_form = ProveedorForm
    template_name = 'add_proveedor.html'


def deleteProveedor(request, **kwargs):

    model = Proveedor
    redirect_to = 'proveedores'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchProveedor(request):

    model = Proveedor

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(telefono__icontains=buscado) |
            Q(email__icontains=buscado) | Q(pagina_web__icontains=buscado)
        )

        return render(request, 'proveedores.html', {"entradas": entradas})
