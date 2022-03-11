from colorfield.widgets import ColorWidget
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget

from otros.models import Evento, Cliente


class EventoForm(ModelForm):

    class Meta:
        model = Evento
        exclude = {}


    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['fecha'].label = "Fecha del evento"
        self.fields['color'].label = "Color"

        # widgets del form
        self.fields['color'].widget.attrs['class'] = 'jscolor'
        self.fields['fecha'].widget = widgets.SelectDateWidget()
        self.fields['nombre'].widget.attrs['class'] = 'form-control'


class ClienteForm(ModelForm):

     class Meta:
         model = Cliente

         exclude = {}