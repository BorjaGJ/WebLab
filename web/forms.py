from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


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