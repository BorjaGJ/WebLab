from datetime import datetime
from django.shortcuts import render
from django.views.generic import CreateView

from web.utils import MyHTMLCalendar


class Index(CreateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        hoy = datetime.now()

        calendario = MyHTMLCalendar().formatmonth(hoy.year, hoy.month)
        return render(request, self.template_name, {'calendario': calendario})