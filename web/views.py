from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from web.forms import WebLabLoginForm


class Index(CreateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class ReactivosView(CreateView):
    template_name = 'reactivos.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
