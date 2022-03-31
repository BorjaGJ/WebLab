import datetime

from annoying.functions import get_object_or_None
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from otros.forms import EventoForm, ClienteForm, ProveedorForm, PedidoForm, AnalisisForm
from otros.models import Evento, Cliente, Proveedor, Analisis, Pedido
from web.views_utils import TableView, EditByIdView, AddView


class EventosTableView(TableView):
    model = Evento
    template_name = 'eventos.html'
    order_by = 'fecha'


class EventoEditView(EditByIdView):
    model = Evento
    redirect_to = 'eventos'
    model_form = EventoForm
    template_name = 'edit_evento.html'


class EventoAddView(AddView):
    model = Evento
    redirect_to = 'eventos'
    model_form = EventoForm
    template_name = 'add_evento.html'




def deleteEvento(request, **kwargs):

    model = Evento
    redirect_to = 'eventos'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchEvento(request):

    model = Evento

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado))
        return render(request, 'clientes.html', {"entradas": entradas})


def delete_expired(request):
    hoy = datetime.datetime.now().date()
    eventos = Evento.objects.all()

    for evento in eventos:
        if evento.fecha < hoy:
            evento.delete()

    return redirect('eventos')

class ClienteTableView(TableView):
    model = Cliente
    template_name = 'clientes.html'
    order_by = 'nombre'

class ClienteAddView(AddView):
    model = Cliente
    redirect_to = 'clientes'
    model_form = ClienteForm
    template_name = 'add_cliente.html'

class ClienteEditView(EditByIdView):
    model = Cliente
    redirect_to = 'clientes'
    model_form = ClienteForm
    template_name = 'edit_cliente.html'

def deleteCliente(request, **kwargs):

    model = Cliente
    redirect_to = 'clientes'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchCliente(request):

    model = Cliente

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(dni__icontains=buscado) |
            Q(telefono__icontains=buscado) | Q(email__icontains=buscado) |
            Q(cp__icontains=buscado) | Q(poblacion__icontains=buscado)
        )

        return render(request, 'clientes.html', {"entradas": entradas})


class ProveedoresTableView(TableView):
    model = Proveedor
    template_name = 'proveedores.html'
    order_by = 'id'


class ProveedoresEditView(EditByIdView):
    model = Proveedor
    redirect_to = 'proveedores'
    model_form = ProveedorForm
    template_name = 'edit_proveedor.html'


class ProveedoresAddView(AddView):
    model = Proveedor
    redirect_to = 'proveedores'
    model_form = ProveedorForm
    template_name = 'add_proveedor.html'


def deleteProveedor(request, **kwargs):

    model = Proveedor
    redirect_to = 'proveedores'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to)

def searchProveedor(request):

    model = Proveedor

    if request.method == 'GET':

        buscado = request.GET.get('buscar')

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(telefono__icontains=buscado) |
            Q(email__icontains=buscado) | Q(pagina_web__icontains=buscado)
        )

        return render(request, 'proveedores.html', {"entradas": entradas})


class PedidosTableView(CreateView):
    template_name = 'pedidos.html'
    model = Pedido
    model_padre = Proveedor
    order_by = 'id'

    def get(self, request, *args, **kwargs):
        entradas = self.model.objects.filter(
            proveedor__nombre_slug__exact=self.kwargs['nombre_slug']).order_by(self.order_by)
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


class AddPedidoView(CreateView):
    template_name = 'add_pedido.html'
    model_form = PedidoForm
    model = Pedido
    model_padre = Proveedor

    def get(self, request, *args, **kwargs):
        form = self.model_form()
        padre = self.model_padre.objects.get(nombre_slug=self.kwargs['nombre_slug'])


        return render(request, self.template_name, {"form": form, 'padre':padre})

    def post(self, request, *args, **kwargs):

        form = self.model_form(request.POST, request.FILES)

        if request.method == 'POST':

            if form.is_valid():
                entrada = form.save(commit=False)
                entrada.proveedor = Proveedor.objects.get(nombre_slug=self.kwargs['nombre_slug'])
                entrada.save()

                return redirect('pedidos', self.kwargs['nombre_slug'])
            else:
                return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {})

class PedidoEditView(CreateView):
    template_name = 'edit_pedido.html'
    model = Pedido
    redirect_to = 'pedidos'
    model_form = PedidoForm
    model_padre = Proveedor

    def get(self, request, *args, **kwargs):

        entrada = self.model.objects.get(id=self.kwargs['id'])
        form = self.model_form(instance=entrada)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})

    def post(self, request, *args, **kwargs):

        entrada = get_object_or_None(self.model, id=self.kwargs['id'])

        form = self.model_form(request.POST, request.FILES, instance=entrada)

        if request.method == 'POST':

            if form.is_valid():
                form.save()
                return redirect(self.redirect_to, entrada.proveedor.nombre_slug)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})




def deletePedido(request, **kwargs):

    model = Pedido
    redirect_to = 'pedidos'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to,  entrada.proveedor.nombre_slug)


def searchPedido(request, **kwargs):

    model = Pedido
    model_padre = Proveedor


    if request.method == 'GET':

        buscado = request.GET.get('buscar')
        padre = model_padre.objects.get(nombre_slug=kwargs['nombre_slug'])

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado) | Q(puntuacion__exact=buscado)
        )

        return render(request, 'pedidos.html', {"entradas": entradas, 'padre': padre})


class AnalisisTableView(CreateView):
    template_name = 'analisis.html'
    model = Analisis
    model_padre = Cliente
    order_by = 'id'

    def get(self, request, *args, **kwargs):
        entradas = self.model.objects.filter(cliente__nombre_slug__exact=self.kwargs['nombre_slug']).order_by(self.order_by)
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


class AddAnalisisView(CreateView):
    template_name = 'add_analisis.html'
    model_form = AnalisisForm
    model = Analisis
    model_padre = Cliente
    redirec_to = 'analisis'

    def get(self, request, *args, **kwargs):
        form = self.model_form()
        padre = self.model_padre.objects.get(nombre_slug=self.kwargs['nombre_slug'])


        return render(request, self.template_name, {"form": form, 'padre':padre})

    def post(self, request, *args, **kwargs):

        form = self.model_form(request.POST, request.FILES)

        if request.method == 'POST':

            if form.is_valid():
                entrada = form.save(commit=False)
                entrada.cliente = Cliente.objects.get(nombre_slug=self.kwargs['nombre_slug'])
                entrada.save()

                return redirect(self.redirec_to, self.kwargs['nombre_slug'])
            else:
                return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {})

class AnalisisEditView(CreateView):
    template_name = 'edit_analisis.html'
    model = Analisis
    redirect_to = 'analisis'
    model_form = AnalisisForm
    model_padre = Cliente

    def get(self, request, *args, **kwargs):

        entrada = self.model.objects.get(id=self.kwargs['id'])
        form = self.model_form(instance=entrada)

        return render(request, self.template_name, {"form": form, 'entrada': entrada, 'padre': entrada.cliente})

    def post(self, request, *args, **kwargs):

        entrada = get_object_or_None(self.model, id=self.kwargs['id'])

        form = self.model_form(request.POST, request.FILES)

        if request.method == 'POST':

            if form.is_valid():

                return redirect(self.redirect_to, entrada.cliente.nombre_slug)

        return render(request, self.template_name, {"form": form, 'entrada': entrada})


def deleteAnalisis(request, **kwargs):

    model = Analisis
    redirect_to = 'analisis'

    entrada = model.objects.get(id=kwargs['id'])
    entrada.delete()

    return redirect(redirect_to,  entrada.cliente.nombre_slug)


def searchAnalisis(request, **kwargs):

    model = Analisis
    model_padre = Cliente


    if request.method == 'GET':

        buscado = request.GET.get('buscar')
        padre = model_padre.objects.get(nombre_slug=kwargs['nombre_slug'])

        entradas = model.objects.filter(
            Q(nombre__icontains=buscado)
        )

        return render(request, 'analisis.html', {"entradas": entradas, 'padre': padre})


