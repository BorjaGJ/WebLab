from calendar import HTMLCalendar
from datetime import date, datetime


class MyHTMLCalendar(HTMLCalendar):

    cssclass_month = 'calendar'
    cssclass_month_head = 'calendar-month-head'
    cssclasses_weekday_head = 'calendar-weekday-head'
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    hoy = datetime.now()


    def formatday(self, day, weekday):

        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % 'calendar-no-day'
        elif day == self.hoy.day:
            # si es hoy
            return '<td class="%s">%d<br>Hoy</td>' % ('calendar-today', day)
        else:
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

