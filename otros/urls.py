from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from otros import views

urlpatterns = [
    url(r'^eventos$', login_required(views.EventosTableView.as_view()), name='eventos'),
    url(r'^eventos/add$', login_required(views.EventoAddView.as_view()), name='add_evento'),
    url(r'^eventos/editar/(?P<id>[-\w]+)$', login_required(views.EventoEditView.as_view()),
        name='evento_edit'),
    url(r'^eventos/delete/(?P<id>[-\w]+)$', login_required(views.deleteEvento), name='delete_evento'),
    url(r'^eventos/delete_expired/$', login_required(views.delete_expired), name='delete_expired'),
    url(r'^search/eventos$', login_required(views.searchEvento), name='search_evento'),

    url(r'^clientes$', login_required(views.ClienteTableView.as_view()), name='clientes'),
    url(r'^clientes/add$', login_required(views.ClienteAddView.as_view()), name='add_cliente'),
    url(r'^clientes/editar/(?P<id>[-\w]+)$', login_required(views.ClienteEditView.as_view()),
        name='cliente_edit'),
    url(r'^clientes/delete/(?P<id>[-\w]+)$', login_required(views.deleteCliente), name='delete_cliente'),
    url(r'^search/clientes$', login_required(views.searchCliente), name='search_cliente'),

    url(r'^proveedores$', login_required(views.ProveedoresTableView.as_view()), name='proveedores'),
    url(r'^proveedores/add$', login_required(views.ProveedoresAddView.as_view()), name='add_proveedor'),
    url(r'^proveedores/editar/(?P<id>[-\w]+)$', login_required(views.ProveedoresEditView.as_view()),
        name='proveedor_edit'),
    url(r'^proveedores/delete/(?P<id>[-\w]+)$', login_required(views.deleteProveedor), name='delete_proveedor'),
    url(r'^search/proveedores$', login_required(views.searchProveedor), name='search_preveedor'),

    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos$', login_required(views.PedidosTableView.as_view()),
        name='pedidos'),
    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos/add$', login_required(views.AddPedidoView.as_view()),
        name='pedidos_add'),
    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos/search$', login_required(views.searchPedido),
        name='pedido_search'),
    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos/(?P<id>[-\w]+)$', login_required(views.PedidoEditView.as_view()),
        name='pedido_edit'),
    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos/detalle/(?P<id>[-\w]+)$', login_required(views.DetallePedidoView.as_view()),
        name='pedido_detalle'),
    url(r'^proveedores/(?P<nombre_slug>[-\w]+)/pedidos/(?P<id>[-\w]+)/delete$', login_required(views.deletePedido),
        name='pedido_delete'),

    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis$', login_required(views.AnalisisTableView.as_view()),
        name='analisis'),
    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis/add$', login_required(views.AddAnalisisView.as_view()),
        name='analisis_add'),
    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis/search$', login_required(views.searchAnalisis),
        name='analisis_search'),
    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis/detalle/(?P<id>[-\w]+)$',
        login_required(views.DetalleAnalisisView.as_view()), name='analisis_detalle'),
    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis/(?P<id>[-\w]+)$', login_required(views.AnalisisEditView.as_view()),
        name='analisis_edit'),
    url(r'^clientes/(?P<nombre_slug>[-\w]+)/analisis/(?P<id>[-\w]+)/delete$', login_required(views.deleteAnalisis),
        name='analisis_delete'),

]
