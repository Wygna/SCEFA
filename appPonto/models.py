from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Funcionario(User):
    nome = models.CharField("Nome", max_length=255)
    Email = models.EmailField("E-mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    matricula = models.CharField("Matricula", max_length=10,unique=True)
    senha = models.CharField(max_length=32)


    def __str__(self):
        return self.nome
    class Meta: permissions = (('view_funcionario', 'Can see aluno'),)

class Administrador(Funcionario):
    class Meta: permissions = (('view_administrador', 'Can see Administrador'),)


class RegistrarPonto(models.Model):
    entrada = models.DateTimeField(default=timezone.now)
    saida = models.DateTimeField(default=timezone.now)
    local = models.CharField("local",max_length=200)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT,verbose_name="Funcionario")

    class Meta: permissions = (('view_relatorio', 'Can see relatorio'),
                               ('view_relatorioPonto', 'Can see relatorio a mais'),)

