from calendar import HTMLCalendar
from datetime import date, datetime
from django.shortcuts import get_object_or_404

from otros.models import Evento
from material.models import Instrumento


class MyHTMLCalendar(HTMLCalendar):

    cssclass_month = 'calendar table-responsive-sm'
    cssclass_month_head = 'calendar-month-head'
    cssclasses_weekday_head = 'calendar-weekday-head'
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dias_semana_min = ["L", "M", "X", "J", "V", "S", "D"]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    hoy = datetime.now()
    lista_dias_eventos = Evento.get_dias_eventos



    def formatday(self, day, weekday):

        if day == 0:
            # dia fuera del mes
            return '<td class="%s">&nbsp;</td>' % 'calendar-no-day'

        elif self.lista_dias_eventos.__contains__(day):
            # dia con evento
            return '<td class="calendar-day" style="background-color:%s;background-image:linear-gradient(to right, %s)">' \
                   '<a class="text-black text-decoration-none" href="calendario/eventos/%d/%d">' \
                   '%d<br><strong>%s Eventos</strong></a></td>' \
                   % \
                   (
                    get_eventos_colores(month=self.hoy.month, day=day),
                    get_eventos_colores(month=self.hoy.month, day=day),
                    self.hoy.month, day, day,
                    get_total_eventos(day=day, month=self.hoy.month)
                    )

        else:
             # cualquier otro dia
            return '<td class="%s">%d</td>' % ('calendar-day', day)

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (self.cssclasses_weekday_head, self.dias_semana_min[day])

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = '%s %s' % (self.meses[themonth-1], theyear)
        else:
            s = '%s' % self.meses[themonth]
        return '<tr><th colspan="7" class="%s">%s</th></tr>' % (
            self.cssclass_month_head, s)





def get_total_eventos(day, month):
    return Evento.objects.filter(fecha__month=month, fecha__day=day).__len__()


def get_eventos_colores(day, month):
    lista_colores = []
    eventos = Evento.objects.filter(fecha__month=month, fecha__day=day)

    for evento in eventos:
        lista_colores.append(evento.color)

    usable = lista_colores.__str__().replace("'", "")

    return usable[1:-1]

