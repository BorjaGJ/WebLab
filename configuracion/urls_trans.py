# -*- coding: utf-8 -*-
from sys import path

from django.contrib.auth.views import LoginView, LogoutView

from web import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from usuarios import views as usuarios_views

from django.contrib import admin
from web.views import *

# from web.views import ControlAsistenciaCreate, Index, Servicios, Requisitos, Garantia, Ventajas, Contacto, \
#     EquipoView, TerminosPoliticasView, CookiesView, NormasComunicacion, NormasComunicacionView, Inscripcion, \
#     InscripcionView, RegistroCompletadoView, GaleriaView, InscripcionesView, EnviarEmailUnDestinatario, MisTrabajosView, \
#     MisDatosView, VerTrabajoView, MisCorreccionesView, VerTrabajosUnUsuario, EditarDatosUsuarioView, CrearTrabajoView, \
#     CrearEntregaView, EditarTrabajoView, VerEntregaView, CrearCorreccionView, PremiosView, SubirPosterView, \
#     VerDetalleUsuarioView, VerTodosTrabajosView, VerTodasEntregasView, EditarUsuarioView, CorreosPendientesView, \
#     EnviarCorreosMasivos, EditarTipoInscripcionView, AsignarCorrectoresView, \
#     InscripcionesOrdenadasNombreView, InscripcionesOrdenadasApellidosView, InscripcionesOrdenadasDNIView, \
#     InscripcionesOrdenadasEmailView, AceptarEntregaComoAdmin, RechazarEntregaComoAdmin, CrearCorreccionFinalView, \
#     EditarComentariosCorreccion, PonerEntregaRevisionComoAdmin, VerCorreosUsuarioView, ComitesView

admin.autodiscover()

urlpatterns = [

    url(r'^$', login_required(Index.as_view()), name='index'),

    url(r'^noticia/(?P<titulo_slug>[-\w]+)$', NoticiaView.as_view(), name='noticia_detalle'),

    url(r'^blog/', include('blog.urls')),

    url(r'^acceso-privado/$', AccesoPrivadoView.as_view(), name='acceso_privado'),

    url(r'^contacto/$', ContactoView.as_view(), name='contacto'),
    url(r'^comunicado-del-presidente/$', CartaPresidenteView.as_view(), name='carta_presidente'),
    url(r'^sede-y-datos-de-contacto/$', SedeView.as_view(), name='sede'),
    url(r'^junta-de-gobierno/$', JuntaDeGobiernoView.as_view(), name='junta_de_gobierno'),
    url(r'^personal-del-colegio/$', PersonalDelColegioView.as_view(), name='personal_colegio'),
    url(r'^asesores/$', AsesoresView.as_view(), name='asesores'),

    url(r'^educacion/$', SaludBucalFaqsView.as_view(), name='faqs'),

    url(r'^drechos-y-deberes-paciente-densista/$', DerechosDeberesPacienteDentistaView.as_view(), name='derechos_deberes_paciente_dentista'),


    url(r'^links-de-interes/$', LinksInteresView.as_view(), name='links_interes'),
    url(r'^gestion-y-tramites/$', TramitesView.as_view(), name='tramites'),
    url(r'^gestion-y-tramites/acuerdos/$', AcuerdosView.as_view(), name='acuerdos'),
    url(r'^gestion-y-tramites/requisitos-de-colegiacion/$', RequisitosDeColegiacionView.as_view(), name='requisitos_colegiacion'),


    url(r'^buscador-de-colegiados/$', BuscadorColegiadosView.as_view(), name='buscador_colegiados'),

    url(r'^buscador-de-colegiados-ajax/$', buscar_colegiados, name='buscador_colegiados_ajax'),

    url(r'^buscador-de-ofertas-empleo-ajax/$', buscar_ofertas_empleo, name='buscador_ofertas_empleo_ajax'),

    url(r'^ordenar-colegiados-num-colegiado/$', ordenar_colegiados_num_colegiado, name='ordenar_colegiados_num_colegiado'),

    url(r'^noticias/$', ListaNoticiasView.as_view(),  name='lista_noticias'),

    url(r'^revista/$', RevistaView.as_view(),  name='revista'),
    url(r'^biblioteca/$', BibliotecaView.as_view(),  name='biblioteca'),

    url(r'^notas-de-prensa/$', NotasDePrensaView.as_view(), name='notas_de_prensa'),

    url(r'^bolsa-de-trabajo-y-compra-venta/$', BolsaDeEmpleoView.as_view(), name='bolsa_empleo'),


    # url(r'^plataforma/inscripciones$', login_required(InscripcionesView.as_view()), name='inscripciones_list'),
    #
    # url(r'^plataforma/inscripciones-ordenadas-por-nombre/$', login_required(InscripcionesOrdenadasNombreView.as_view()),
    #     name='inscripciones_ordernar_nombre'),
    #
    # url(r'^plataforma/inscripciones-ordenadadas-por-apellidos/$', login_required(InscripcionesOrdenadasApellidosView.as_view()),
    #     name='inscripciones_ordernar_apellidos'),
    #
    # url(r'^plataforma/inscripciones-ordenadas-por-DNI/$', login_required(InscripcionesOrdenadasDNIView.as_view()),
    #     name='inscripciones_ordernar_dni'),




    url(r'^login', LoginView.as_view(template_name='login_acceso_privado.html'), name='login_app'),

    # primer paso recoger el correo del usuario y enviar el email
    url(r'^reiniciar-password/$',
        auth_views.PasswordResetView.as_view(template_name='app/autenticacion/password_reset_form.html',
                                             email_template_name='app/autenticacion/password_reset_email.html',
                                             html_email_template_name='app/autenticacion/password_reset_email.html',
                                             subject_template_name="app/autenticacion/password_reset_subject.html"),
        name='reset_password_inicio'),

    # segundo paso se ha enviado un email
    url(r'^reiniciar-password-enviado', auth_views.PasswordResetDoneView.as_view(template_name='app/autenticacion/password_reset_done.html'),
        name='password_reset_done'),


    # tercer paso confirmar password nueva
    url(r'^reiniciar-password-nueva/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='app/autenticacion/password_reset_confirm.html'),
        name='password_reset_confirm'),

    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # cuarto paso se completa el proceso
    url(r'^reinciar-password-completado/$', auth_views.PasswordResetCompleteView.as_view(template_name='app/autenticacion/password_reset_complete.html'),
        name='password_reset_complete'
        ),


    # url(r'^(?P<idioma>[-\w]+)$', views.CambiarIdioma.as_view(), name='idioma'),
    #
    # url(r'^jet/', include('jet.urls', 'jet')),
    # url(r'^usuarios/', include('usuarios.urls')),




]

# if settings.DEBUG:
# import debug_toolbar
# urlpatterns += patterns('',
#    url(r'^__debug__/', include(debug_toolbar.urls)),
# )
