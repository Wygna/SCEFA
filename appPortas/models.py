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
    hora_acesso = models.TimeField(default=timezone.now)
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")

    def calcurar_tempo_trabalho(self):
        pass

    class Meta: permissions = (('view_Registro_porta', 'Can see Registro_porta'),)

class Usuario(models.Model):
    pessoa = models.OneToOneField(Pessoa,verbose_name='Usuário')

    def __str__(self):
        return self.pessoa.nome

    class Meta: permissions = (('view_usuario', 'Can see usuario'),)

class Grupo(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    class Meta: permissions = (('view_grupo', 'Can see grupo'),)

    def __str__(self):
        return self.descricao

    class Meta: permissions = (('view_grupo', 'Can see grupo'),)

class Porta_Grupo(models.Model):
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT,verbose_name="Grupo")

    class Meta: permissions = (('view_porta_grupo', 'Can see porta_grupo'),)

class Usuario_Grupo(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT,verbose_name="Grupo")
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT,verbose_name="Usuário")

    class Meta: permissions = (('view_usuario_grupo', 'Can see usuario_grupo'),)

