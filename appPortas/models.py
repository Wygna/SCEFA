from django.utils import timezone

from appPonto.models import *


class Porta(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    local = models.CharField('Local', max_length=255)

    def __str__(self):
        return self.descricao
    class Meta: permissions = (('view_porta', 'Can see porta'),)

class Registro_Porta(models.Model):
    data = models.DateField(default=timezone.now)
    hora_acesso = models.TimeField(default=timezone.now)
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")
    pessoa = models.ForeignKey(Pessoa,on_delete=models.PROTECT,verbose_name='Pessoa')

    def diaSemana(self):
        semana = ['Segunda-Feira', 'Terceira-Feira', 'Quarta-Feira',
                  'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return semana[self.data.weekday()]

    class Meta: permissions = (('view_Registro_porta', 'Can see Registro_porta'),)

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

class Pessoa_Grupo(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT,verbose_name="Grupo")
    pessoa = models.ForeignKey(Pessoa,on_delete=models.PROTECT,verbose_name="Pessoa")

    class Meta: permissions = (('view_pessoa_grupo', 'Can see pessoa_grupo'),)

