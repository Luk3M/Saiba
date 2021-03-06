"""
Definition of urls for Saiba.
"""

from datetime import datetime

import django.contrib.auth.views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import PostSitemap

admin.autodiscover()

handler403 = 'home.views.custom_403'
handler404 = 'home.views.custom_404'
handler418 = 'home.views.custom_418'
handler500 = 'home.views.custom_500'

sitemaps = { 
    'post': PostSitemap,
}


urlpatterns = [
    # Entry database
    url(r'^', include('home.urls')),
    url(r'^', include('content.urls')),
    url(r'^entrada/', include('entry.urls')),
    url(r'^galeria/', include('gallery.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^perfil/', include('profile.urls')),
    url(r'^staff/', include('staff.urls')),
    url(r'^feedback/', include('feedback.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
