from otros.models import Trabajador
from trabajadores.forms import TrabajadorForm
from web.views_utils import AddView


class TrabajadoresAddView(AddView):
    template_name = 'add_trabajador.html'
    model = Trabajador
    model_form = TrabajadorForm
    redirect_to = 'index'