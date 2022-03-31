import calendar
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from otros.models import Evento
from web.forms import ConfiguracionEventosForm
from web.models import ConfiguracionEventos
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


class EventosCalendarioView(CreateView):
    template_name = 'eventos.html'

    def get(self, request, *args, **kwargs):
        eventos = Evento.objects.filter(fecha__month=self.kwargs['mes'], fecha__day=self.kwargs['dia'])

        return render(request, self.template_name, {'entradas': eventos})


class ConfiguracionEventosView(CreateView):
    template_name = 'configuracion_eventos.html'

    def get(self, request, *args, **kwargs):

        entrada = ConfiguracionEventos.objects.all().last()

        if entrada is None:
            entrada = ConfiguracionEventos.objects.create()

        form = ConfiguracionEventosForm(instance=entrada)

        return render(request, self.template_name, {'form': form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = ConfiguracionEventos.objects.all().last()

        form = ConfiguracionEventosForm(request.POST, instance=entrada)

        if request.method == 'POST':

            if form.is_valid():
                form.save()
                return redirect('index')

        return render(request, self.template_name, {"form": form, 'entrada': entrada})


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
