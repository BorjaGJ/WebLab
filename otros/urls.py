from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from otros import views

urlpatterns = [
    url(r'^eventos$', login_required(views.EventosTableView.as_view()), name='eventos'),
    url(r'^eventos/add$', login_required(views.EventoAddView.as_view()), name='add_evento'),
    url(r'^eventos/editar/(?P<id>[-\w]+)$', login_required(views.EventoEditView.as_view()),
        name='evento_edit'),
    url(r'^eventos/delete/(?P<id>[-\w]+)$', login_required(views.deleteEvento), name='delete_evento'),
    url(r'^eventos/delete_expired/$', login_required(views.delete_expired), name='delete_expired')

]
