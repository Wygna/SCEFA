from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from tastypie.api import Api

from appPonto.views import *
from .api import *

api=Api(api_name='dados')
pessoaResource=PessoaResource()
frequenciaResource = FrequenciasResource()
registroPortaResource = RegistroPortaResource()
portaResource = PortaResource()
api.register(pessoaResource)
api.register(frequenciaResource)
api.register(portaResource)
api.register(registroPortaResource)

urlpatterns = [
    url(r'^api/', include(api.urls)),
    url(r'^$', home, name='home'),
    url(r'^login/', login, {'template_name': 'utils/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^erro_permissao/$', erro_permissao, name='erro_permissao'),

    url(r'^funcionario/list$', funcionario_list, name='funcionario_list'),
    url(r'^funcionario/detail/(?P<pk>\d+)$',funcionario_detail, name='funcionario_detail'),
    url(r'^funcionario/new/$', funcionario_new, name='funcionario_new'),
    url(r'^funcionario/update/(?P<pk>\d+)$', funcionario_update, name='funcionario_update'),
    url(r'^funcionario/delete/(?P<pk>\d+)$',funcionario_delete, name='funcionario_delete'),

    url(r'^departamento/list$', departamento_list, name='departamento_list'),
    url(r'^departamento/detail/(?P<pk>\d+)$',departamento_detail, name='departamento_detail'),
    url(r'^departamento/new/$', departamento_new, name='departamento_new'),
    url(r'^departamento/update/(?P<pk>\d+)$', departamento_update, name='departamento_update'),
    url(r'^departamento/delete/(?P<pk>\d+)$',departamento_delete, name='departamento_delete'),

    url(r'^cargo/list$', cargo_list, name='cargo_list'),
    url(r'^cargo/detail/(?P<pk>\d+)$',cargo_detail, name='cargo_detail'),
    url(r'^cargo/new/$', cargo_new, name='cargo_new'),
    url(r'^cargo/update/(?P<pk>\d+)$', cargo_update, name='cargo_update'),
    url(r'^cargo/delete/(?P<pk>\d+)$',cargo_delete, name='cargo_delete'),

    url(r'^DiasSemExdiente/list$', diasSemExpediente_list, name='diasSemExpediente_list'),
    url(r'^DiasSemExdiente/new/$', diasSemExpediente_new, name='diasSemExpediente_new'),
    url(r'^DiasSemExdiente/update/(?P<pk>\d+)$', diasSemExpediente_update, name='diasSemExpediente_update'),
    url(r'^DiasSemExdiente/delete/(?P<pk>\d+)$',diasSemExpediente_delete, name='diasSemExpediente_delete'),

    url(r'^horario/list$', horario_list, name='horario_list'),
    url(r'^horario/detail/(?P<pk>\d+)$', horario_detail, name='horario_detail'),
    url(r'^horario/new/$', horario_new, name='horario_new'),
    url(r'^horario/update/(?P<pk>\d+)$', horario_update, name='horario_update'),
    url(r'^horario/delete/(?P<pk>\d+)$', horario_delete, name='horario_delete'),

    url(r'^administrador/list$', administrador_list, name='administrador_list'),
    url(r'^administrador/new/$', administrador_new, name='administrador_new'),
    url(r'^administrador/add/(?P<pk>\d+)$',adicionar_administrador, name='administrador_add'),
    url(r'^administrador/delete/(?P<pk>\d+)$', remover_administrador, name='remover_administrador'),
    url(r'^administrador/update/(?P<pk>\d+)$', administrador_update, name='administrador_update'),

    url(r'^busca/frequencia/$', busca_frequencia, name='busca_frequencia'),
    url(r'^ponto/frequencia_funcionario/$', funcionario_frequencia, name='funcionario_frequencia'),
    url(r'^perfil_funcionario/$', perfil_funcionario, name='perfil_funcionario'),

    url(r'^funcionarios/$', funcionarios, name='funcionarios'),
    url(r'^busca/frequencia_funcionario/(?P<pk>\d+)$', busca_frequencia_funcionario,
        name='busca_frequencia_funcionario'),
    url(r'^funcionario/frequencias/(?P<pk>\d+)$', funcionario_frequencias, name='funcionario_frequencias'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
