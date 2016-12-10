from django.conf.urls import url
from alunos.views import *

urlpatterns = [
    url(r'^alunos/list$', aluno_list, name='aluno_list'),
    url(r'^alunos/new/$', aluno_new, name='alunos_new'),
    url(r'^alunos/detail/(?P<pk>\d+)$', aluno_detail, name='alunos_detail'),
]
