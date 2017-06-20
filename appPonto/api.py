from django.template.context_processors import request
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from appPortas.models import *
from tastypie import fields
from appPonto.models import *
from tastypie.exceptions import NotFound
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.models import ApiKey
from tastypie.authorization import DjangoAuthorization,ReadOnlyAuthorization
from appPonto.teste import *


class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        resource_name='pessoa'
        filtering = {'nome': ALL}
        limit = 0
        max_limit = 0
        fields = ['nome','email','telefone']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class FuncionarioResource(ModelResource):
    pessoa = fields.ForeignKey(PessoaResource, attribute='pessoa',full=True)
    class Meta:
        queryset = Funcionario.objects.all()
        resource_name='funcionario'
        fields = ['matricula']
        authentication = BasicAuthentication()

class CargosResource(ModelResource):
    class Meta:
        queryset = Cargo.objects.all()
        resource_name='cargo'
        authentication = BasicAuthentication()

class PortasResource(ModelResource):
    class Meta:
        queryset = Porta.objects.all()
        resource_name='portas'
        authentication = BasicAuthentication()

class FrequenciasResource(ModelResource):
    pessoa = fields.ForeignKey(PessoaResource, attribute='pessoa',full=True)

    class Meta:
        queryset = Frequencia.objects.all()
        resource_name='frequencias'
        limit = 0
        max_limit = 0
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class PessoaFrequenciasResource(ModelResource):
    frequencia = fields.OneToManyField(FrequenciasResource, 'frequencia',full=True)
    class Meta:
        queryset = Pessoa.objects.all()
        resource_name='pessoafrequencias'
        authentication = BasicAuthentication()






