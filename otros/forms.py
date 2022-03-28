from django.forms import ModelForm, widgets
from flatpickr import DatePickerInput

from otros.models import Evento, Cliente, Proveedor, Pedido


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
        self.fields['fecha'].widget = DatePickerInput()
        self.fields['nombre'].widget.attrs['class'] = 'form-control'


class ClienteForm(ModelForm):

     class Meta:
         model = Cliente

         exclude = {}

class ProveedorForm(ModelForm):

    class Meta:
        model = Proveedor

        exclude = {'nota'}


class PedidoForm(ModelForm):

    class Meta:
        model = Pedido

        exclude = {}

        widgets = {
            'fecha_espera': DatePickerInput(),
            'fecha_recibido': DatePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)

        self.fields['nombre'].label = "Nombre"
        self.fields['fecha_espera'].label = "Fecha esperado"
        self.fields['fecha_recibido'].label = "Fecha recibido"
        self.fields['albaran'].label = "Albarán"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['puntuacion'].label = "Puntuación"





