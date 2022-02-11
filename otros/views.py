from otros.forms import EventoForm
from otros.models import Evento
from web.views_utils import TableView, EditByIdView, AddView


class EventosTableView(TableView):
    model = Evento
    template_name = 'eventos.html'


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
