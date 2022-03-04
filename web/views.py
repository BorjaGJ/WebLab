import calendar
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic import CreateView

from otros.models import Evento
from web.utils import MyHTMLCalendar


class Index(CreateView):
    template_name = 'base.html'
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def get(self, request, *args, **kwargs):
        hoy = datetime.now()
        semana = self.dias_semana[hoy.weekday()]
        mes = hoy.month
        ano = hoy.year

        calendario = MyHTMLCalendar().formatmonth(ano, mes)
        return render(request, self.template_name, {'calendario': calendario, 'hoy': hoy, 'semana': semana})

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

