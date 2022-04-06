from django import  template
from django.contrib.auth.models import User

from web.models import CustomPermisos

register = template.Library()

@register.simple_tag(name='get_perimisos')
def get_permisos(usuario):
    print(usuario)
    return CustomPermisos.objects.get(usuario=usuario)
#
