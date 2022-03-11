import datetime

from django.db.models import Q
from django.shortcuts import redirect, render

from otros.forms import EventoForm, ClienteForm
from otros.models import Evento, Cliente
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
        return render(request, 'patrones.html', {"entradas": entradas})


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
            Q(telefono__icontains=buscado) | Q(email__icontains=buscado)
        )

        return render(request, 'patrones.html', {"entradas": entradas})