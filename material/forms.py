from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, widgets

from material.models import Volumetrico


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
