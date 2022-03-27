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
from email import message

from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views.generic import TemplateView

import web

from django.conf.urls.i18n import i18n_patterns

from configuracion import settings
from web.forms import WebLabLoginForm
from django.contrib.auth.decorators import login_required

from web.views import Index

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
    url(r'^trabajadores/', include('trabajadores.urls')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url('^qr_code/', include('qr_code.urls', namespace="qr_code")),

]



# urlpatterns += i18n_patterns(
#     # url(r'^', include('configuracion.urls_trans'))
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)