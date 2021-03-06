from django.conf.urls import url
from . import views

app_name = 'staff'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^nova-postagem$', views.create_post, name = 'create_post'),
    url(r'^procurar-usuario', views.search_user, name = 'search_user'),
    url(r'^redirecionar', views.entry_redirect, name = 'entry_redirect'),
]