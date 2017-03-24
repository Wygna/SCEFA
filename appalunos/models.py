from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Aluno(User):
    nome = models.CharField("Nome", max_length=200)
    Email = models.EmailField("E-mail", max_length=200)
    Turnos = (
        ('Matutino', 'Matutino'),
        ('Vespetino', 'Vespetino'),
        ('Noturno', 'Noturno'),
    )
    turno_aula = models.CharField(
        max_length=30,
        choices=Turnos,
    )
    senha = models.CharField(max_length=32)
    matricula = models.CharField("Matricula", max_length=14, unique=True)


    def __str__(self):
        return self.nome

    class Meta: permissions = (('view_aluno', 'Can see aluno'),)

class RegistrarPonto(models.Model):
    entrada = models.DateTimeField(default=timezone.now)
    saida = models.DateTimeField(default=timezone.now)
    local = models.CharField("local",max_length=200)
    aluno = models.ForeignKey(Aluno,on_delete=models.PROTECT,verbose_name="Aluno")

    class Meta: permissions = (('view_relatorio_aluno', 'Can see relatorio aluno'),
                               ('view_relatorioPonto_aluno', 'Can see relatorio mais aluno'),)