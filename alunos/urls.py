from django.conf.urls import url
from alunos.views import alunos_new

urlpatterns = [
    url(r'^alunos/new/$', alunos_new, name='alunos_new')
]
