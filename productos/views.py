from annoying.functions import get_object_or_None
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView

from productos.forms import ReactivoForm
from productos.models import Reactivo, Disolvente, Patron


class ReactivosView(CreateView):
    template_name = 'reactivos.html'

    def get(self, request, *args, **kwargs):
        reactivos = Reactivo.objects.all()
        return render(request, self.template_name, {"productos": reactivos})


# class ReactivosDetailView(DetailView):
#     template_name = 'reactivos_edit.html'
#     model = Reactivo
#
#     def get(self, request, *args, **kwargs):
#         entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])
#         return render(request, self.template_name, {"producto": entrada})


class ReactivosEditView(CreateView):
    template_name = 'reactivos_edit.html'
    model = Reactivo

    def get(self, request, *args, **kwargs):
        entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])
        form = ReactivoForm(instance=entrada)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])

        if request.method == 'POST':
            form = ReactivoForm(request.POST, instance=entrada)

            if form.is_valid():
                form.save()
                return redirect('reactivos')

        return render(request, self.template_name, {})


def DeleteReactivo(request, *args, **kwargs):

    model = Reactivo
    entrada = Reactivo.objects.get(codigo_laboratorio=kwargs['codigo_laboratorio'])
    entrada.delete()

    return redirect('reactivos')


class AddReactivo(CreateView):
    template_name = 'add_reactivo.html'

    def get(self, request, *args, **kwargs):
        form = ReactivoForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = ReactivoForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('reactivos')

        return render(request, self.template_name, {})



class DisolventesView(CreateView):
    template_name = 'disolventes.html'

    def get(self, request, *args, **kwargs):

        disolventes = Disolvente.objects.all()

        return render(request, self.template_name, {"productos": disolventes})

class PatronesView(CreateView):
    template_name = 'patrones.html'

    def get(self, request, *args, **kwargs):

        patrones = Patron.objects.all()

        return render(request, self.template_name, {"productos": patrones})