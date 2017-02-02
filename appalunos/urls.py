from django.conf.urls import url
from appalunos.views import *

urlpatterns = [
    url(r'^aluno/list$', aluno_list, name='aluno_list'),
    url(r'^aluno/detail/(?P<pk>\d+)$', aluno_detail, name='aluno_detail'),
    url(r'^aluno/update/(?P<pk>\d+)$', aluno_update, name='aluno_update'),
    url(r'^aluno/new/$', aluno_new, name='aluno_new'),
    url(r'^aluno/delete/(?P<pk>\d+)$', aluno_delete, name='aluno_delete'),
    url(r'^aluno/relatorio/(?P<pk>\d+)$',
        aluno_relatorio, name='aluno_relatorio'),
    url(r'^aluno/relatorio/(?P<pk>\d+)$',
       aluno_relatorio, name='aluno_relatorio'),
]