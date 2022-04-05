from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserChangeForm

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from web.models import ConfiguracionEventos


class WebLabLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(WebLabLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label='Usuario', widget=forms.TextInput(
        attrs={
            'class': 'input-field mb-3',
            'placeholder': 'Nombre de usuario',
            'id': 'user',
            'label': 'usuario'
        }))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'input-field',
            'placeholder': 'Contraseña',
            'id': 'password',
        }


))

class ConfiguracionEventosForm(ModelForm):

    class Meta:

        model = ConfiguracionEventos

        exclude = {}

        labels = {
            'color_instrumentos': 'Color de los eventos de los instrumentos',
            'color_volumetricos': 'Color de los eventos del material volumétrico',
            'color_miscelaneas': 'Color de los eventos de misceláneas',
            'color_patrones': 'Color de los eventos de los patrones',
            'color_reactivos': 'Color de los eventos de los reactivos',
            'color_disolventes': 'Color de los eventos de los disolventes',
            'color_pedidos': 'Color de los eventos de los pedidos',
            'color_analisis': 'Color de los eventos de los analisis',
        }

    def __init__(self, *args, **kwargs):
        super(ConfiguracionEventosForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'jscolor'


