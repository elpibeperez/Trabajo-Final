from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sistema/', include('sistema.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^mensajes/$', 'sistema.mensajes.views.index'),
    (r'^mensajes/crear/$', 'sistema.mensajes.views.crear'),
    (r'^mensajes/nuevo_mensaje/$', 'sistema.mensajes.views.nuevo_mensaje'),
    (r'^mensajes/leer/(?P<mensaje_id>\d+)/$', 'sistema.mensajes.views.leer'),
    (r'^mensajes/responder/$', 'sistema.mensajes.views.responder'),
    (r'^mensajes/borrar/$', 'sistema.mensajes.views.borrar'),
    (r'^login/$',   'sistema.views.login'),
    (r'^desloguear/$', 'sistema.views.desloguear'),
    (r'^$',         'sistema.views.index'),
)

