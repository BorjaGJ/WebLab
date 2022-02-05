from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from material import views

urlpatterns = [
    url(r'^volumetrico$', login_required(views.VolumetricosView.as_view()), name='volumetrico'),
    url(r'^volumetrico/add$', login_required(views.VolumetricoAddView.as_view()), name='add_volumetrico'),
    url(r'^volumetrico/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.VolumetricoEditView.as_view()),
        name='volumetrico_edit'),
    url(r'^delete/volumetrcio/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteVolumetrico),
        name='delete_volumetrico'),
    url(r'^search/reactivo$', login_required(views.SearchVolumetrico), name='search_volumetrico'),

    ]