from django.conf.urls import url

from appAlunos.views import *

urlpatterns = [
    url(r'^aluno/list$', aluno_list, name='aluno_list'),
    url(r'^aluno/detail/(?P<pk>\d+)$', aluno_detail, name='aluno_detail'),
    url(r'^aluno/update/(?P<pk>\d+)$', aluno_update, name='aluno_update'),
    url(r'^aluno/new/$', aluno_new, name='aluno_new'),
    url(r'^aluno/delete/(?P<pk>\d+)$', aluno_delete, name='aluno_delete'),
    url(r'^aluno/frequencias/(?P<pk>\d+)$', aluno_frequencias, name='aluno_frequencias'),
    url(r'^ponto/frequencia_aluno/$', aluno_frequencia, name='aluno_frequencia'),
    url(r'^alunos/$', alunos, name='alunos'),
    url(r'^perfil_aluno/$', perfil_aluno, name='perfil_aluno'),
    url(r'^busca/frequencia_aluno/(?P<pk>\d+)$', busca_frequencia_aluno, name='busca_frequencia_aluno'),
]
