from ckeditor.widgets import CKEditorWidget
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, widgets
from flatpickr import DatePickerInput

from material.models import no_space_validator, no_asciis_validator
from productos.models import Reactivo, Disolvente, Patron


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
        self.fields['proveedor'].label = "Proveedor"
        self.fields['fecha_caducidad'].label = "Fecha de caducidad"
        self.fields['ficha_seguridad'].label = "Ficha de seguridad"
        self.fields['pureza'].label = "Pureza"
        self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]
        self.fields['pureza'].validators = [MinValueValidator(0), MaxValueValidator(100)]


        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == 'organico':
                pass

            elif visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'fecha_caducidad':
                visible.field.widget = DatePickerInput()

            else:
                visible.field.widget.attrs['class'] = 'form-control'


class DisolventeForm(ModelForm):

        class Meta:
            model = Disolvente
            exclude = {}

        def __init__(self, *args, **kwargs):
            super(DisolventeForm, self).__init__(*args, **kwargs)

            # poner las etiquetas
            self.fields['nombre'].label = 'Nombre'
            self.fields['CAS'].label = "CAS"
            self.fields['codigo_laboratorio'].label = "Código de laboratorio"
            self.fields['organico'].label = "Orgánico"
            self.fields['cantidad'].label = "Cantidad"
            self.fields['proveedor'].label = "Proveedor"
            self.fields['fecha_caducidad'].label = "Fecha de caducidad"
            self.fields['ficha_seguridad'].label = "Ficha de seguridad"
            self.fields['densidad'].label = "Densidad"
            self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]

            # añadir las clases
            for visible in self.visible_fields():

                if visible.name == 'organico':
                    pass

                elif visible.name == "ubicacion":
                    visible.field.widget = CKEditorWidget()

                elif visible.name == 'fecha_caducidad':
                    visible.field.widget = DatePickerInput()

                else:
                    visible.field.widget.attrs['class'] = 'form-control'




class PatronForm(ModelForm):

    class Meta:
        model = Patron
        exclude = {}


    def __init__(self, *args, **kwargs):
        super(PatronForm, self).__init__(*args, **kwargs)

        # poner las etiquetas
        self.fields['nombre'].label = 'Nombre'
        self.fields['CAS'].label = "CAS"
        self.fields['codigo_laboratorio'].label = "Código de laboratorio"
        self.fields['organico'].label = "Orgánico"
        self.fields['cantidad'].label = "Cantidad"
        self.fields['proveedor'].label = "Proveedor"
        self.fields['fecha_caducidad'].label = "Fecha de caducidad"
        self.fields['concentracion'].label = "Concentración"
        self.fields['ficha_seguridad'].label = "Ficha de seguridad"
        self.fields['certificado'].label = "Certificado"
        self.fields['codigo_laboratorio'].validators = [no_space_validator, no_asciis_validator]

        # añadir las clases
        for visible in self.visible_fields():

            if visible.name == 'organico':
                pass

            elif visible.name == "ubicacion":
                visible.field.widget = CKEditorWidget()

            elif visible.name == 'fecha_caducidad':
                visible.field.widget = DatePickerInput()

            else:
                visible.field.widget.attrs['class'] = 'form-control'
