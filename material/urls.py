from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from material import views

urlpatterns = [
    url(r'^volumetricos$', login_required(views.VolumetricosView.as_view()), name='volumetrico'),
    url(r'^volumetrico/add$', login_required(views.VolumetricoAddView.as_view()), name='add_volumetrico'),
    url(r'^volumetrico/detalle/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DetailVolumetricoView.as_view()),
        name='volumetrico_detalle'),
    url(r'^volumetrico/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.VolumetricoEditView.as_view()),
        name='volumetrico_edit'),
    url(r'^delete/volumetrico/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.deleteVolumetrico),
        name='delete_volumetrico'),
    url(r'^search/reactivo$', login_required(views.searchVolumetrico), name='search_volumetrico'),

    url(r'^instrumentos$', login_required(views.InstrumentosView.as_view()), name='instrumento'),
    url(r'^instrumento/add$', login_required(views.InstrumentoAddView.as_view()), name='add_instrumento'),
    url(r'^instrumento/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.InstrumentoEditView.as_view()),
        name='instrumento_edit'),
    url(r'^instrumento/detalle/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DetailInstrumentoView.as_view()),
        name='instrumento_detalle'),
    url(r'^delete/instrumento/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.deleteInstrumento),
        name='delete_instrumento'),
    url(r'^search/instrumento$', login_required(views.searchInstrumento), name='search_instrumento'),

    url(r'^miscelaneas$', login_required(views.MiscelaneasView.as_view()), name='miscelanea'),
    url(r'^miscelanea/add$', login_required(views.MiscelaneaAddView.as_view()), name='add_miscelanea'),
    url(r'^miscelanea/detalle/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.DetailMiscelaneaView.as_view()),
        name='miscelanea_detalle'),
    url(r'^miscelanea/editar/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.MiscelaneaEditView.as_view()),
        name='miscelanea_edit'),
    url(r'^delete/miscelanea/(?P<codigo_laboratorio>[-\w]+)$', login_required(views.deleteMiscelanea),
        name='delete_miscelanea'),
    url(r'^search/miscelanea$', login_required(views.searchMiscelanea), name='search_miscelanea'),

    url(r'verificar$', login_required(views.Verificar.as_view()), name='verificar'),


]