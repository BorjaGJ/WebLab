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
            return '<td class="%s" style="background-color: %s">%d<br>%s</td>' % \
                   ('calendar-day',
                    get_evento(day=day, month=self.hoy.month).color,
                    day,
                    get_eventos_nombres(day=day, month=self.hoy.month)
                    )

        else:
             # cualquier otro
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




def get_evento(day, month,):
    return  Evento.objects.filter(fecha__month=month, fecha__day=day).first()

def get_eventos_nombres(day, month):
    lista_nombres = []
    eventos = Evento.objects.filter(fecha__month=month, fecha__day=day)

    for evento in eventos:
        lista_nombres.append(evento.nombre+'<br>')

    usable = lista_nombres.__str__().replace("', '", '')

    return usable[2:-2:1]

