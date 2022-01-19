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


import web

from django.conf.urls.i18n import i18n_patterns

from configuracion import settings
from web.forms import WebLabLoginForm
from web import views as web_views
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(web_views.Index.as_view()), name='index'),

    url(r'^login/$', auth_views.LoginView.as_view(authentication_form=WebLabLoginForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reactivos$', login_required(web_views.ReactivosView.as_view()), name='reactivos'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]



# urlpatterns += i18n_patterns(
#     # url(r'^', include('configuracion.urls_trans'))
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)