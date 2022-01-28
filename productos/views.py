from django.shortcuts import render
from django.views.generic import CreateView

from productos.models import Reactivo


class ReactivosView(CreateView):
    template_name = 'reactivos.html'

    def get(self, request, *args, **kwargs):

        reactivos = Reactivo.objects.all()

        return render(request, self.template_name, {"productos": reactivos})