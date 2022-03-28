from django.forms import ModelForm, widgets

from otros.models import Trabajador


class TrabajadorForm(ModelForm):

    class Meta:
        model = Trabajador

        exclude = {'user'}

        widgets = {

        }

    def clean(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password_confirm'):
            self.add_error('password_confirm', "Las contraseñas no coinciden!")
        return cd