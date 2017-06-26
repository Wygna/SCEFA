from django.conf.urls import url

from appAlunos.views import *

urlpatterns = [
    url(r'^aluno/list$', aluno_list, name='aluno_list'),
    url(r'^aluno/detail/(?P<pk>\d+)$', aluno_detail, name='aluno_detail'),
    url(r'^aluno/update/(?P<pk>\d+)$', aluno_update, name='aluno_update'),
    url(r'^aluno/new/$', aluno_new, name='aluno_new'),
    url(r'^aluno/delete/(?P<pk>\d+)$', aluno_delete, name='aluno_delete'),
    url(r'^aluno/frequencias/(?P<pk>\d+)$',
        aluno_frequencias, name='aluno_frequencias'),
    url(r'^aluno/frequencia/(?P<pk>\d+)$',
            aluno_frequencia, name='aluno_frequencia'),

    url(r'^busca/aluno/frequencia/(?P<pk>\d+)$',
        busca_aluno_frequencia, name='busca_aluno_frequencia'),
    url(r'^frequencia/list$', alunos_list, name='Frequencia_list'),

]