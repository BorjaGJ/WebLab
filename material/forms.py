from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, widgets
from flatpickr import DatePickerInput

from material.models import Volumetrico, Instrumento, Miscelanea, no_space_validator, no_asciis_validator


class VolumetricoForm(ModelForm):

    class Meta:
        model = Volumetrico
        exclude = {}

    def __init__(self, *args, **kwargs):
        super(VolumetricoForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['codigo_laboratorio'].label = "Código de laboratorio"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['graduacion'].label = "Graduación"
        self.fields['volumen'].label = "Volumen"
        self.fields['cuantia'].label = "Número de unidades"
        self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]
        self.fields['proxima_revision'].label = "Proxima revisión"

        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = DatePickerInput()

            else:
                visible.field.widget.attrs['class'] = 'form-control'


class InstrumentoForm(ModelForm):

    class Meta:
        model = Instrumento
        exclude = {}

    def __init__(self, *args, **kwargs):
        super(InstrumentoForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['codigo_laboratorio'].label = "Código de laboratorio"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['proxima_revision'].label = "Proxima revisión"
        self.fields['metodo_calibracion'].label = "Método de Calibración"
        self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]


        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = DatePickerInput()

            else:
                visible.field.widget.attrs['class'] = 'form-control'


class MiscelaneaForm(ModelForm):

    class Meta:
        model = Miscelanea
        exclude = {}

    def __init__(self, *args, **kwargs):
        super(MiscelaneaForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['codigo_laboratorio'].label = "Código de laboratorio"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]
        self.fields['proxima_revision'].label = "Proxima revisión"

        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = DatePickerInput()

            else:
                visible.field.widget.attrs['class'] = 'form-control'
