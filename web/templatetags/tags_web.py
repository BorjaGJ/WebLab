from annoying.functions import get_object_or_None
from django import  template
from django.contrib.auth.models import User

from web.models import CustomPermisos, ConfiguracionEventos

register = template.Library()


class PermisoTotal:
    can_add = True
    can_edit = True
    can_delete = True
    can_user = True
    can_color = True


@register.simple_tag(name='get_permisos')
def get_permisos(usuario):

    permisos = get_object_or_None(CustomPermisos, usuario=usuario)

    if permisos is None:
        permisos = PermisoTotal

    return permisos


@register.simple_tag(name='get_pased_text')
def get_parsed_text(request, escrito, variable):
    return 'https://' + request.get_host() + str(escrito) + str(variable)


@register.simple_tag(name='get_pased_text_from_2')
def get_parsed_text_from_2(request, escrito, variable, escrito2, variable2):
    return 'https://' + request.get_host() + str(escrito) + str(variable) + str(escrito2) + str(variable2)

@register.simple_tag(name='get_color_conf')
def get_color_conf():
    return ConfiguracionEventos.objects.first()




