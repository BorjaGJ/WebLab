from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from productos import views

urlpatterns = [
    url(r'^reactivos$', login_required(views.ReactivoTableView.as_view()), name='reactivos'),
    url(r'^reactivos/add$', login_required(views.ReactivoAddView.as_view()), name='add_reactivo'),
    url(r'^reactivos/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.ReactivoEditView.as_view()),
        name='reactivo_edit'),
    url(r'^delete/reactivo/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteReactivo), name='delete_reactivo'),
    url(r'^search/$', login_required(views.searchReactivo), name='search_reactivo'),

    url(r'^disolventes$', login_required(views.DisolventeView.as_view()), name='disolventes'),
    url(r'^disolventes/add$', login_required(views.DisolventeAddView.as_view()), name='add_disolvente'),
    url(r'^disolventes/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DisolventeEditView.as_view()),
        name='disolvente_edit'),
    url(r'^delete/disolvente/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteDisolvente),
        name='delete_reactivo'),



    url(r'^patrones$', login_required(views.PatronesView.as_view()), name='patrones'),


]