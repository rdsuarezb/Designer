from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'DawProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('',include('social.apps.django_app.urls',namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('web.urls'))
    
]
