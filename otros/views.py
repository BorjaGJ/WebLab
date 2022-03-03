from django.db.models import Q
from django.shortcuts import redirect, render

from otros.forms import EventoForm
from otros.models import Evento
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

        buscado = request.GET.get('buscarPatron')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado))
        return render(request, 'patrones.html', {"entradas": entradas})
