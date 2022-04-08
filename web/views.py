import calendar
from datetime import datetime, timedelta

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from otros.models import Evento
from web.forms import ConfiguracionEventosForm, CustomPermisosForm
from web.models import ConfiguracionEventos, CustomPermisos
from web.utils import MyHTMLCalendar
from web.views_utils import AddView


class Index(CreateView):
    template_name = 'base.html'
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def get(self, request, *args, **kwargs):
        hoy = datetime.now()
        semana = self.dias_semana[hoy.weekday()]
        mes = hoy.month
        ano = hoy.year

        calendario = MyHTMLCalendar().formatmonth(ano, mes)

        return render(request, self.template_name, {'calendario': calendario, 'hoy': hoy, 'semana': semana})


class EventosCalendarioView(CreateView):
    template_name = 'eventos.html'

    def get(self, request, *args, **kwargs):
        eventos = Evento.objects.filter(fecha__month=self.kwargs['mes'], fecha__day=self.kwargs['dia'])

        return render(request, self.template_name, {'entradas': eventos})


class ConfiguracionEventosView(CreateView):
    template_name = 'configuracion_eventos.html'

    def get(self, request, *args, **kwargs):

        entrada = ConfiguracionEventos.objects.all().last()

        if entrada is None:
            entrada = ConfiguracionEventos.objects.create()

        form = ConfiguracionEventosForm(instance=entrada)

        return render(request, self.template_name, {'form': form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = ConfiguracionEventos.objects.all().last()

        form = ConfiguracionEventosForm(request.POST, instance=entrada)

        if request.method == 'POST':

            if form.is_valid():
                form.save()
                print('save')
                return redirect('index')

        return render(request, self.template_name, {"form": form, 'entrada': entrada})


class AddUserView(AddView):
    template_name = 'add_user.html'
    model = User
    model_form = UserCreationForm
    redirect_to = 'index'

    def post(self, request, *args, **kwargs):

        form = self.model_form(request.POST)

        if form.is_valid():
            permisos = request.POST.getlist('permisos')
            usuario = form.save()

            custompermisos = CustomPermisos.objects.create(usuario=usuario)

            if permisos.__contains__('edit'):
                custompermisos.can_edit = True

            if permisos.__contains__('delete'):
                custompermisos.can_delete = True

            if permisos.__contains__('add'):
                custompermisos.can_add = True

            if permisos.__contains__('color'):
                custompermisos.can_color = True

            if permisos.__contains__('user'):
                custompermisos.can_user = True

            custompermisos.save()

            return redirect(self.redirect_to)

        return render(request, self.template_name, {'form': form})

class EditUser(CreateView):
    template_name = 'edit_user.html'

    def get(self, request, *args, **kwargs):

        form = PasswordChangeForm(request.user)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = PasswordChangeForm(request.user)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, self.template_name, {'form': form})


class UserListView(CreateView):
    template_name = 'usuarios.html'

    def get(self, request, *args, **kwargs):
        usuarios = User.objects.filter(is_staff=False)
        return render(request, self.template_name, {'usuarios': usuarios})


class EditPermisosUserView(CreateView):
    template_name = 'edit_permisos.html'

    def get(self, request, *args, **kwargs):
        usuario = User.objects.get(id=self.kwargs['id'])
        entrada = CustomPermisos.objects.get(usuario=usuario)
        form = CustomPermisosForm(instance=entrada)
        return render(request, self.template_name, {'form': form, 'usuario': usuario})

    def post(self, request, *args, **kwargs):
        usuario = User.objects.get(id=self.kwargs['id'])
        entrada = CustomPermisos.objects.get(usuario=usuario)
        form = CustomPermisosForm(request.POST, instance=entrada)

        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')

        return render(request, self.template_name, {'form': form, 'usuario': usuario})


def deleteUsuario(request, **kwargs):

    entrada = User.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect('lista_usuarios')

def searchUsuario(request):

    model = User

    if request.method == 'GET':
        buscado = request.GET.get('buscar')

        usuarios = model.objects.filter(
            Q(username__icontains=buscado)
        )

        return render(request, 'clientes.html', {"usuarios": usuarios})

class LectorView(CreateView):
    template_name = 'lector.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
