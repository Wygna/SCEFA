from django.conf.urls import url
from django.contrib.auth.views import login,logout

from appPortas.views import *

urlpatterns = [
    url(r'^porta/list$', porta_list, name='porta_list'),
    url(r'^porta/detail/(?P<pk>\d+)$',porta_detail, name='porta_detail'),
    url(r'^porta/new/$', porta_new, name='porta_new'),
    url(r'^porta/update/(?P<pk>\d+)$',porta_update, name='porta_update'),
    url(r'^porta/delete/(?P<pk>\d+)$',porta_delete, name='porta_delete'),

    url(r'^grupo/porta/add$', porta_list, name='grupo_porta_add'),

    url(r'^grupo/list$', grupo_list, name='grupo_list'),
    url(r'^grupo/detail/(?P<pk>\d+)$',grupo_detail, name='grupo_detail'),
    url(r'^grupo/new/$', grupo_new, name='grupo_new'),
    url(r'^grupo/update/(?P<pk>\d+)$',grupo_update, name='grupo_update'),
    url(r'^grupo/delete/(?P<pk>\d+)$',grupo_delete, name='grupo_delete'),

    url(r'^acesso/grupo/list$', acesso_grupo_list, name='acesso_grupo_list'),

    url(r'^usuario/list$', grupo_list, name='usuario_list'),
    url(r'^usuario/detail/(?P<pk>\d+)$',grupo_detail, name='usuario_detail'),
    url(r'^usuario/acesso/grupo/list/(?P<pk>\d+)$', usuario_acesso_grupo_list, name='usuario_acesso_grupo_list'),
    url(r'^usuario/sem_acesso/grupo/(?P<pk>\d+)$', usuario_sem_acesso_grupo, name='usuario_sem_acesso_grupo'),

    url(r'^porta/no_grupo/list/(?P<pk>\d+)$', porta_no_grupo_list, name='porta_no_grupo_list'),
    url(r'^porta/nao_grupo/(?P<pk>\d+)$', porta_nao_grupo_list, name='porta_nao_grupo'),

    #url(r'^usuario/add/aluno', usuario_aluno_add, name='usuario_aluno_add'),
    url(r'^usuario/update/(?P<pk>\d+)$',porta_update, name='usuario_update'),
    url(r'^usuario/delete/(?P<pk>\d+)$',porta_delete, name='usuario_delete'),



]
