from django.db import models
from appPonto.models import *
from django.utils import timezone

class Porta(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    local = models.CharField('Local', max_length=255)

    def __str__(self):
        return self.descricao
    class Meta: permissions = (('view_porta', 'Can see porta'),)

class Registro_porta(models.Model):
    data = models.DateField(default=timezone.now)
    hora_entrada = models.TimeField(default=timezone.now)
    hora_saida = models.TimeField(default=timezone.now)
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")

    class Meta: permissions = (('view_PermissaoPorta', 'Can see PermissaoPorta'),)

class Usuario(Pessoa):
    class Meta: permissions = (('view_usuario', 'Can see usuario'),)

class grupo(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    usuario = models.ManyToManyField(Usuario)
    porta = models.ManyToManyField(Porta)