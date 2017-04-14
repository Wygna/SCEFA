from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from appPonto.models import Pessoa

class Aluno(Pessoa):
    Turnos = (
        ('Matutino', 'Matutino'),
        ('Vespetino', 'Vespetino'),
        ('Noturno', 'Noturno'),
    )
    turno_aula = models.CharField(
        max_length=30,
        choices=Turnos,
    )

    def __str__(self):
        return self.nome

    class Meta: permissions = (('view_aluno', 'Can see aluno'),)

class RegistrarPonto(models.Model):
    data = models.DateTimeField(default=timezone.now)
    local = models.CharField("local",max_length=200)
    aluno = models.ForeignKey(Aluno,on_delete=models.PROTECT,verbose_name="Aluno")

    class Meta: permissions = (('view_relatorio_aluno', 'Can see relatorio aluno'),
                               ('view_relatorioPonto_aluno', 'Can see relatorio mais aluno'),)