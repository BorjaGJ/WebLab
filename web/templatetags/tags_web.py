from annoying.functions import get_object_or_None
from django import  template
from django.contrib.auth.models import User

from web.models import CustomPermisos

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
def get_parsed_text(escrito, variable):
    return str(escrito) + str(variable)


@register.simple_tag(name='get_pased_text_from_2')
def get_parsed_text_from_2(escrito, variable, escrito2, variable2):
    return str(escrito) + str(variable) + str(escrito2) + str(variable2)

