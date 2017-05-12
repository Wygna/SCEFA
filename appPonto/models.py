from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Pessoa(User):
    nome = models.CharField("Nome", max_length=255)
    Email = models.EmailField("E-mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    matricula = models.CharField("Matricula", max_length=10,unique=True)
    senha = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    descricao = models.CharField("Descrição",max_length=200)
    class Meta: permissions = (('view_departamento', 'Can see departamento'),)
    def __str__(self):
        return self.descricao

class Cargo(models.Model):
    nome_funcao = models.CharField('Nome da função',max_length=200)
    departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT,verbose_name="Departamento")
    class Meta: permissions = (('view_cargo', 'Can see cargo'),)
    def __str__(self):
        return self.nome_funcao

class Funcionario(Pessoa):
    cargo = models.ForeignKey(Cargo,on_delete=models.PROTECT,verbose_name="Cargo")

    def setCargo(self,funcao):
        cargo = Cargo.objects.get(nome_funcao=funcao)
        self.cargo = cargo

    def __str__(self):
        return self.nome
    class Meta: permissions = (('view_funcionario', 'Can see funcionario'),)

class Frequencia(models.Model):
    data = models.DateField(default=timezone.now)
    hora_entrada = models.TimeField(default=timezone.now)
    hora_saida = models.TimeField(default=timezone.now)
    local = models.CharField("local",max_length=200)

    def hora_inicial_final(self):
        formatacao = '%H:%M:%S'
        t = datetime.datetime.strptime(str(self.hora_saida), formatacao) - datetime.datetime.strptime(str(self.hora_entrada), formatacao)
        return t
    def tempo_maximo(self):
        formatacao = '%H:%M:%S'
        tempo = str(datetime.datetime.strptime(str(self.hora_saida), formatacao) - datetime.datetime.strptime(str(self.hora_entrada), formatacao))
        t = int(tempo[0])
        return t

    def diaSemana(self):
        semana= ['Segunda-Feira', 'Terceira-Feira', 'Quarta-Feira',
        'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return semana[self.data.weekday()]

class Frequencia_funcionario(Frequencia):
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT,verbose_name="Funcionario")
    class Meta: permissions = (('view_frequencia_funcionario', 'Can see frequencia'),
                               ('view_frequencia_funcionario_admin', 'Can see frequencia a mais'),)

class Dias_sem_expediente(models.Model):
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.data.






