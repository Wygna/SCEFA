from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from appPonto.models import *
from appPortas.models import *
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        resource_name = 'pessoa'
        fields = ['username', 'nome', 'Email']
        filtering = {'nome': ALL}
        list_allowed_methods = ['get', 'post']
        authentication = BasicAuthentication()
        authorization = Authorization()
        include_resource_uri = False

    # def obj_create(self, bundle, **kwargs):
      # return super(PessoaResource, self).obj_create(bundle, user=bundle.request.user)

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(username=bundle.request.user)


class FrequenciasResource(ModelResource):
    pessoa = fields.ForeignKey(PessoaResource, 'pessoa', full=True)
    class Meta:
        queryset = Frequencia.objects.filter(~Q(hora_entrada=None)).order_by('data')
        resource_name = 'frequencias'
        limit = 0
        max_limit = 0
        filtering = {
            "data": ['gte', 'lte'],
        }
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authentication = BasicAuthentication()
        authorization = Authorization()

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(pessoa=bundle.request.user)


class PortaResource(ModelResource):
    class Meta:
        queryset = Porta.objects.all()
        resource_name = 'porta'
        fields = ['descricao']
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authentication = BasicAuthentication()
        authorization = Authorization()


class RegistroPortaResource(ModelResource):
    pessoa = fields.ForeignKey(PessoaResource, 'pessoa', full=True)
    porta = fields.ForeignKey(PortaResource, 'porta', full=True)

    class Meta:
        queryset = RegistroPorta.objects.all()
        resource_name = 'registro_portas'
        limit = 0
        max_limit = 0
        filtering = {
            "data": ['gte', 'lte'],
        }
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authentication = BasicAuthentication()
        authorization = Authorization()

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(pessoa=bundle.request.user)
