"""proyectolimpio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from configuracion import settings
from web.forms import WebLabLoginForm
from django.contrib.auth.decorators import login_required

from web.views import Index, EventosCalendarioView, ConfiguracionEventosView, AddUserView, EditUser, LectorView, \
    UserListView, deleteUsuario, searchUsuario, EditPermisosUserView

admin.autodiscover()

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(Index.as_view()), name='index'),

    url(r'^login/$', auth_views.LoginView.as_view(authentication_form=WebLabLoginForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^productos/', include('productos.urls')),
    url(r'^material/', include('material.urls')),
    url(r'^otros/', include('otros.urls')),

    url(r'^usuarios/$', login_required(UserListView.as_view()), name='lista_usuarios'),
    url(r'^usuarios/add$', login_required(AddUserView.as_view()), name='add_trabajador'),
    url(r'^usuarios/delete/(?P<id>[-\d]+)$', login_required(deleteUsuario), name='delete_usuario'),
    url(r'^usuarios/search$', login_required(searchUsuario), name='search_usuario'),
    url(r'^usuarios/mi_usuario/change_password$', login_required(EditUser.as_view()), name='edit_user'),
    url(r'^usuarios/editar/(?P<id>[-\d]+)$', login_required(EditPermisosUserView.as_view()), name='edit_permisos'),


    url(r'^calendario/eventos/(?P<mes>[-\d]+)/(?P<dia>[-\d]+)$', login_required(EventosCalendarioView.as_view()),
        name='calendario_eventos'),
    url(r'^configuracion/colores_eventos/$', login_required(ConfiguracionEventosView.as_view()),
        name='configuracion_color'),
    url('^lector_qr/$', login_required(LectorView.as_view()), name='lector'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url('^qr_code/', include('qr_code.urls', namespace="qr_code")),
    url(r'^robots\.txt', include('robots.urls')),

]



# urlpatterns += i18n_patterns(
#     # url(r'^', include('configuracion.urls_trans'))
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)