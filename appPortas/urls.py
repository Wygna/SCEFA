from django.conf.urls import url
from django.contrib.auth.views import login,logout

from appPortas.views import *

urlpatterns = [
    url(r'^porta/list$', porta_list, name='porta_list'),
    url(r'^porta/detail/(?P<pk>\d+)$',porta_detail, name='porta_detail'),
    url(r'^porta/new/$', porta_new, name='porta_new'),
    url(r'^porta/update/(?P<pk>\d+)$',porta_update, name='porta_update'),
    url(r'^porta/delete/(?P<pk>\d+)$',porta_delete, name='porta_delete'),

    url(r'^grupo/list$', grupo_list, name='grupo_list'),
    url(r'^grupo/detail/(?P<pk>\d+)$',grupo_detail, name='grupo_detail'),
    url(r'^grupo/new/$', grupo_new, name='grupo_new'),
    url(r'^grupo/update/(?P<pk>\d+)$',grupo_update, name='grupo_update'),
    url(r'^grupo/delete/(?P<pk>\d+)$',grupo_delete, name='grupo_delete'),

    url(r'^edit/grupo/$', edit_grupo, name='edit_grupo'),

    url(r'^grupo/usuario/list/(?P<pk>\d+)$', grupo_usuario_list, name='grupo_usuario_list'),
    url(r'^usuario/acesso/grupo/(?P<pk>\d+)$', usuario_acesso_grupo, name='usuario_acesso_grupo'),
    url(r'^usuario/sem_acesso/grupo/(?P<pk>\d+)$', usuario_sem_acesso_grupo, name='usuario_sem_acesso_grupo'),

    url(r'^porta/no_grupo/(?P<pk>\d+)$', porta_no_grupo, name='porta_no_grupo'),
    url(r'^porta/nao_grupo/(?P<pk>\d+)$', porta_nao_grupo, name='porta_nao_grupo'),



]
