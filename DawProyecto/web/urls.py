from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    # url(r'^$', 'DawProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$',"web.views.CargarPrincipal"),
    url(r'^Perfil/$',"web.views.CargarPerfil"),
    url(r'^Documentos/$',"web.views.CargarDocumentos"),
    url(r'^AreaDeTrabajo/$',"web.views.CargarAreaDeTrabajo"),
    url(r'^login$',"web.views.login"),
    url(r'^logout$',"web.views.logout"),
]
