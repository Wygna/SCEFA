from django.conf.urls import url,include
from django.contrib.auth.views import login,logout

from appPonto.views import *
from .api import *
from tastypie.api import Api

api=Api(api_name='dados')

pessoaResource=PessoaResource()

frequenciaResource = FrequenciasResource()

api.register(pessoaResource)

api.register(frequenciaResource)


urlpatterns = [
    url(r'^api/', include(api.urls)),
    url(r'^$', home, name='home'),
    url(r'^login/', login, {'template_name': 'utils/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^erro_permissao/$', erro_permissao, name='erro_permissao'),

    url(r'^funcionario/list$', funcionario_list, name='funcionario_list'),
    url(r'^funcionario/detail/(?P<pk>\d+)$',funcionario_detail, name='funcionario_detail'),
    url(r'^funcionario/new/$', funcionario_new, name='funcionario_new'),
    url(r'^funcionario/update/(?P<pk>\d+)$', funcionairo_update, name='funcionario_update'),
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

    url(r'^administrador/list$', administrador_list, name='administrador_list'),
    #url(r'^administrador/detail/(?P<pk>\d+)$', administrador_detail, name='administrador_detail'),
    url(r'^administrador/new/$', administrador_new, name='administrador_new'),
    url(r'^administrador/add/(?P<pk>\d+)$',adicionar_administrador, name='administrador_add'),

    url(r'^administrador/update/(?P<pk>\d+)$', funcionairo_administrardor_update, name='administrador_update'),
    url(r'^administrador/delete/(?P<pk>\d+)$', remover_administrador, name='remover_administrador'),

    url(r'^Frequencia/list$', funcionarios_list, name='frequencia_list'),

    url(r'^funcionario/frequencia/(?P<pk>\d+)$',
       funcionario_frequencia, name='funcionario_frequencia'),

    url(r'^funcionario/frequencias/(?P<pk>\d+)$',
        funcionario_frequencias, name='funcionario_frequencias'),

    url(r'^busca/funcionario/frequencia/(?P<pk>\d+)$',
        busca_funcionario_frequencia, name='busca_funcionario_frequencia'),





]
