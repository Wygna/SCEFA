from django.utils import timezone

from appPonto.models import *


class Porta(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    local = models.CharField('Local', max_length=255)

    def __str__(self):
        return self.descricao
    class Meta: permissions = (('view_porta', 'Can see porta'),)


class RegistroPorta(models.Model):
    data = models.DateField(default=timezone.now)
    hora_acesso = models.TimeField(default=timezone.now)
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")
    pessoa = models.ForeignKey(Pessoa,on_delete=models.PROTECT,verbose_name='Pessoa')

    def diaSemana(self):
        semana = ['Segunda-Feira', 'Terceira-Feira', 'Quarta-Feira',
                  'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return semana[self.data.weekday()]

    @classmethod
    def validarData(cls, data):
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])
        validade = "true"
        i = 0
        while validade == "true" and i == 0:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                bissexto = "sim"
            else:
                bissexto = "nao"
            if mes < 1 or mes > 12:
                validade = "false"
            if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
                validade = "false"
            if (mes == 2 and bissexto == "nao" and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
                validade = "false"
            i = i + 1
        if validade == "true":
            return True
        else:
            return False

    class Meta:
        permissions = (('view_registro_porta', 'Can see registro_porta'),)

class Grupo(models.Model):
    descricao = models.CharField('Descrição', max_length=255)
    class Meta: permissions = (('view_grupo', 'Can see grupo'),)

    def __str__(self):
        return self.descricao

    class Meta: permissions = (('view_grupo', 'Can see grupo'),)


class GrupoPorta(models.Model):
    porta = models.ForeignKey(Porta,on_delete=models.PROTECT,verbose_name="Porta")
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT,verbose_name="Grupo")

    class Meta: permissions = (('view_grupo_porta', 'Can see grupo_porta'),)


class GrupoPessoa(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT,verbose_name="Grupo")
    pessoa = models.ForeignKey(Pessoa,on_delete=models.PROTECT,verbose_name="Pessoa")

    class Meta: permissions = (('view_grupo_pessoa', 'Can see grupo_pessoa'),)
