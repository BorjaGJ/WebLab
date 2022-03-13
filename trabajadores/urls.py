from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from trabajadores import views

urlpatterns = [
    url(r'^trabajadores/add$', login_required(views.TrabajadoresAddView.as_view()), name='add_trabajador'),
]