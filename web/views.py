from django.shortcuts import render
from django.views.generic import CreateView


class Index(CreateView):
    template_name = 'base.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})