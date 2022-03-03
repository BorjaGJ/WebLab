from calendar import HTMLCalendar
from datetime import date, datetime
from django.shortcuts import get_object_or_404

from otros.models import Evento
from material.models import Instrumento


class MyHTMLCalendar(HTMLCalendar):

    cssclass_month = 'calendar'
    cssclass_month_head = 'calendar-month-head'
    cssclasses_weekday_head = 'calendar-weekday-head'
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
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
            return '<td class="%s" style="background-color: %s">%d<br>%s</td>' % \
                   ('calendar-day', get_evento(day=day, month=self.hoy.month).color,
                    day,
                    get_evento(day=day, month=self.hoy.month).nombre
                    )

        else:
             # cualquier otro
            return '<td class="%s">%d</td>' % ('calendar-day', day)

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (self.cssclasses_weekday_head, self.dias_semana[day])

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




def get_evento(day, month):
    return Evento.objects.get(fecha__month=month, fecha__day=day)

