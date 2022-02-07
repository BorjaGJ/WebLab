from calendar import HTMLCalendar, calendar
from datetime import date, datetime

from annoying.functions import get_object_or_None
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from productos.forms import ReactivoForm
from productos.models import Reactivo
from web.utils import MyHTMLCalendar

class TableView(CreateView):
    template_name = 'reactivos.html'
    model = Reactivo

    def get(self, request, *args, **kwargs):
        entradas = self.model.objects.all()
        return render(request, self.template_name, {"entradas": entradas})


class EditView(CreateView):
    template_name = 'edit_reactivo.html'
    model = Reactivo
    redirect_to = 'reactivos'
    model_form = ReactivoForm

    def get(self, request, *args, **kwargs):

        entrada = self.model.objects.get(codigo_laboratorio=self.kwargs['codigo_laboratorio'])
        form = self.model_form(instance=entrada)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])

        form = self.model_form(request.POST, instance=entrada)

        if request.method == 'POST':

            if form.is_valid():

                form.save()
                return redirect(self.redirect_to)

        return render(request, self.template_name, {})


class AddView(CreateView):
    template_name = 'add_reactivo.html'
    model_form = ReactivoForm
    redirect_to = 'reactivos'

    def get(self, request, *args, **kwargs):
        form = self.model_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        form = self.model_form(request.POST)

        if request.method == 'POST':

            if form.is_valid():
                form.save()
                return redirect(self.redirect_to)

        return render(request, self.template_name, {})



