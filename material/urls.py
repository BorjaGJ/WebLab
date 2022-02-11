from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from material import views

urlpatterns = [
    url(r'^volumetricos$', login_required(views.VolumetricosView.as_view()), name='volumetrico'),
    url(r'^volumetrico/add$', login_required(views.VolumetricoAddView.as_view()), name='add_volumetrico'),
    url(r'^volumetrico/edit/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.VolumetricoEditView.as_view()),
        name='volumetrico_edit'),
    url(r'^delete/volumetrico/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteVolumetrico),
        name='delete_volumetrico'),
    url(r'^search/reactivo$', login_required(views.SearchVolumetrico), name='search_volumetrico'),

    url(r'^instrumentos$', login_required(views.InstrumentosView.as_view()), name='instrumento'),
    url(r'^instrumento/add$', login_required(views.InstrumentoAddView.as_view()), name='add_instrumento'),
    url(r'^instrumento/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.InstrumentoEditView.as_view()),
        name='instrumento_edit'),
    url(r'^delete/instrumento/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteInstrumento),
        name='delete_instrumento'),
    url(r'^search/instrumento$', login_required(views.SearchInstrumento), name='search_instrumento'),

    url(r'^miscelaneas$', login_required(views.MiscelaneasView.as_view()), name='miscelanea'),
    url(r'^miscelanea/add$', login_required(views.MiscelaneaAddView.as_view()), name='add_miscelanea'),
    url(r'^miscelanea/edit/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.MiscelaneaEditView.as_view()),
        name='miscelanea_edit'),
    url(r'^delete/miscelanea/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DeleteMiscelanea),
        name='delete_miscelanea'),
    url(r'^search/instrumento$', login_required(views.SearchMiscelanea), name='search_miscelanea'),

    ]