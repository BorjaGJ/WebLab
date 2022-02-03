from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from productos import views

urlpatterns = [
    url(r'^reactivos$', login_required(views.ReactivosView.as_view()), name='reactivos'),
    url(r'^reactivos/add$', login_required(views.AddReactivo.as_view()), name='add_reactivo'),
    url(r'^reactivos/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.ReactivosEditView.as_view()), name='reactivo_edit'),
    url(r'^delete/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteReactivo), name='delete_reactivo'),
    url(r'^search/$', login_required(views.searchReactivo), name='search_reactivo'),

    url(r'^disolventes$', login_required(views.DisolventesView.as_view()), name='disolventes'),
    url(r'^patrones$', login_required(views.PatronesView.as_view()), name='patrones'),


]