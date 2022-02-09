from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, widgets

from material.models import Volumetrico, Instrumento, Miscelanea


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
        self.fields['lote'].label = "lote"
        self.fields['volumen'].label = "Volumen"
        self.fields['proxima_revision'].label = "Proxima revisión"
        self.fields['cuantia'].label = "Número de unidades"

        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = widgets.SelectDateWidget()

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
        self.fields['manual'].label = "Manual"
        self.fields['metodo_calibracion'].label = "método de Calibración"


        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = widgets.SelectDateWidget()

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
        self.fields['proxima_revision'].label = "Proxima revisión"



        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'proxima_revision':
                visible.field.widget = widgets.SelectDateWidget()

            else:
                visible.field.widget.attrs['class'] = 'form-control'
