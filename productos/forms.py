from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, widgets

from productos.models import Reactivo


class ReactivoForm(ModelForm):

    class Meta:
        model = Reactivo
        exclude = {}


    def __init__(self, *args, **kwargs):
        super(ReactivoForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['CAS'].label = "CAS"
        self.fields['codigo_laboratorio'].label = "Código de laboratorio"
        self.fields['organico'].label = "Orgánico"
        self.fields['cantidad'].label = "Cantidad"
        self.fields['ficha_seguridad'].label = "Ficha de seguridad"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['fecha_caducidad'].label = "Fecha de caducidad"
        self.fields['pureza'].label = "Pureza"

        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == 'organico':
                pass

            elif visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'fecha_caducidad':
                visible.field.widget = widgets.SelectDateWidget()

            else:
                visible.field.widget.attrs['class'] = 'form-control'





