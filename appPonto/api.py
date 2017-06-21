from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpRequest
from django.template.context_processors import request
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from appPortas.models import *
from tastypie import fields
from appPonto.models import *
from tastypie.exceptions import NotFound
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, ReadOnlyAuthorization
from appPonto.teste import *


class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        resource_name = 'pessoa'
        fields = ['username', 'nome', 'email']
        list_allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()
        authorization = Authorization()

    #def obj_create(self, bundle, **kwargs):
     #   return super(PessoaResource, self).obj_create(bundle, user=bundle.request.user)

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(username=bundle.request.user)


class FrequenciasResource(ModelResource):
    pessoa = fields.ForeignKey(PessoaResource,'pessoa',full=True)
    class Meta:
        queryset = Frequencia.objects.all()
        resource_name = 'frequencias'
        limit = 0
        max_limit = 0
        list_allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()
        authorization = Authorization()

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(pessoa=bundle.request.user)










