from django.conf.urls import url
from django.contrib.auth.views import login,logout

from appPonto.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/', login, {'template_name': 'utils/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^erro_permissao/$', erro_permissao, name='erro_permissao'),

    url(r'^funcionario/list$', funcionario_list, name='funcionario_list'),
    url(r'^funcionario/detail/(?P<pk>\d+)$',
        funcionario_detail, name='funcionario_detail'),
    url(r'^funcionario/new/$', funcionario_new, name='funcionario_new'),
    url(r'^funcionario/update/(?P<pk>\d+)$',
        funcionairo_update, name='funcionario_update'),
    url(r'^funcionario/delete/(?P<pk>\d+)$',
        funcionario_delete, name='funcionario_delete'),

    url(r'^administrador/list$', administrador_list, name='administrador_list'),
    url(r'^administrador/detail/(?P<pk>\d+)$',
        administrador_detail, name='administrador_detail'),
    url(r'^administrador/new/$', administrador_new, name='administrador_new'),
    url(r'^administrador/update/(?P<pk>\d+)$',
        administrador_update, name='administrador_update'),
    url(r'^administrador/delete/(?P<pk>\d+)$',
        administrador_delete, name='administrador_delete'),

    url(r'^RegistroPonto/list$', registroPonto_list, name='registroPonto_list'),

    url(r'^funcionario/relatorio/(?P<pk>\d+)$',
       funcionario_relatorio, name='funcionario_relatorio'),



]
