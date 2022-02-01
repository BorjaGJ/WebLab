from annoying.functions import get_object_or_None
from django.shortcuts import render
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
#     template_name = 'reactivos_detalle.html'
#     model = Reactivo
#
#     def get(self, request, *args, **kwargs):
#         entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])
#         return render(request, self.template_name, {"producto": entrada})

class ReactivosEditView(DetailView):
    template_name = 'reactivos_detalle.html'
    model = Reactivo

    def get(self, request, *args, **kwargs):
        entrada = get_object_or_None(self.model, codigo_laboratorio=self.kwargs['codigo_laboratorio'])
        form = ReactivoForm(instance=entrada)
        return render(request, self.template_name, {"form": form, 'entrada': entrada})



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