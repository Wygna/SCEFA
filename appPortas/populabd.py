from django.contrib.auth.models import Group
from appPortas.models import *

grupo = Grupo(descricao='Professores de Mecatrônica')
grupo2 = Grupo(descricao='Professores de Informática')
grupo3 = Grupo(descricao='Professores de Redes')
grupo4 = Grupo(descricao='Coordenadores de Cursos')

grupo.save()
grupo2.save()
grupo3.save()
grupo4.save()

porta = Porta(descricao='Laborátorio de Mecatrônica')
porta2 = Porta(descricao='Laborátorio de Informática')
porta3 = Porta(descricao='Laborátorio de Redes')
porta4 = Porta(descricao='Sala de Coordenação de Cursos')

porta.save()
porta2.save()
porta3.save()
porta4.save()

