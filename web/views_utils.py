from calendar import HTMLCalendar, calendar
from datetime import date, datetime

from annoying.functions import get_object_or_None
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from otros.models import Proveedor, Pedido
from productos.forms import ReactivoForm
from productos.models import Reactivo


class TableView(CreateView):
    template_name = 'reactivos.html'
    model = Reactivo
    order_by = 'id'

    def get(self, request, *args, **kwargs):
        entradas = self.model.objects.all().order_by(self.order_by)
        print(entradas)
        page = request.GET.get('page', 1)

        paginator = Paginator(entradas, 15)
        try:
            entradas = paginator.page(page)
        except PageNotAnInteger:
            entradas = paginator.page(1)
        except EmptyPage:
            entradas = paginator.page(paginator.num_pages)
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


        return render(request, self.template_name, {"form": form, 'entrada': entrada})


class EditByIdView(CreateView):
    template_name = 'edit_reactivo.html'
    model = Reactivo
    redirect_to = 'reactivos'
    model_form = ReactivoForm

    def get(self, request, *args, **kwargs):

        entrada = self.model.objects.get(id=self.kwargs['id'])
        form = self.model_form(instance=entrada)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = get_object_or_None(self.model, id=self.kwargs['id'])

        form = self.model_form(request.POST, instance=entrada)

        if request.method == 'POST':

            if form.is_valid():
                form.save()
                return redirect(self.redirect_to)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})


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
            else:
                return render(request, self.template_name, {"form": form})


        return render(request, self.template_name, {})


class TableViewEntry(CreateView):
    template_name = 'pedidos.html'
    model = Pedido
    model_padre = Proveedor
    order_by = 'id'

    def get(self, request, *args, **kwargs):
        entradas = self.model.objects.filter(proveedor__nombre_slug__exact=self.kwargs['nombre_slug']).order_by(self.order_by)
        padre = self.model_padre.objects.get(nombre_slug=self.kwargs['nombre_slug'])
        page = request.GET.get('page', 1)
        paginator = Paginator(entradas, 15)
        try:
            entradas = paginator.page(page)
        except PageNotAnInteger:
            entradas = paginator.page(1)
        except EmptyPage:
            entradas = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {"entradas": entradas, "padre": padre})
