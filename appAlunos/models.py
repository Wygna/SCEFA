from django.contrib.auth.models import User
from django.db import models

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
    matricula = models.CharField("Matricula", max_length=20, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        permissions = (('view_aluno',
                        'Can see aluno'),)
