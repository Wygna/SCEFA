from django.contrib.auth.models import Group

from appAlunos.models import Aluno
from appPonto.models import *

aluno = Aluno(username='183', first_name='Paulo Cesar', nome='Paulo Cesar', Email='paulo@gmail.com',
              telefone='(84)99102-3323', situacao='Ativo', matricula='183',
              turno_aula='Matutino', cpf='100.400.220-01', dataNascimento='1981-02-22',
              endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno2 = Aluno(username='129', first_name='Luiz Felipe', nome='Luiz Felipe', Email='luiz@gmail.com', situacao='Ativo',
               matricula='129', turno_aula='Matutino',
               cpf='200.400.220-01', dataNascimento='1982-02-22', endereco='Rua Bernando Viera, Natal - RN',
               sexo='Masculino', telefone='(84)99102-3023')
aluno3 = Aluno(username='138', first_name='Ednilson da Silva Palhares', nome='Ednilson da Silva Palhares', Email='ednilson@gmail.com',
               telefone='(84)99122-3323', situacao='Ativo',
               matricula='138', turno_aula='Vespetino', cpf='300.400.220-01', dataNascimento='1983-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino', )
aluno4 = Aluno(username='118', first_name='Judas', nome='Judas', Email='judas@gmail.com', telefone='(84)91102-3323',
               situacao='Ativo',
               matricula='118', turno_aula='Matutino', cpf='400.400.22-01', dataNascimento='1988-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno5 = Aluno(username='1197', first_name='Daniel', nome='Daniel', Email='daniel@gmail.com', telefone='(84)94102-3323',
               situacao='Ativo', matricula='1197',
               turno_aula='Matutino', cpf='500.400.220-01', dataNascimento='1989-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno6 = Aluno(username='2183', first_name='Juliana Soares', nome='Juliana Soares', Email='juliana@gmail.com',
               telefone='(84)99202-3323', situacao='Ativo',
               matricula='2183', turno_aula='Vespetino', cpf='600.400.220-01', dataNascimento='1982-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Feminino')
aluno7 = Aluno(username='2129', first_name='Lucas Lima', nome='Lucas Lima', Email='lucas@gmail.com', situacao='Ativo',
               matricula='2129', turno_aula='Vespetino',
               cpf='700.400.220-01', dataNascimento='1992-02-22', endereco='Rua Bernando Viera, Natal - RN',
               sexo='Masculino', telefone='(84)99002-3323')
aluno8 = Aluno(username='2138', first_name='Matheus Oliveria', nome='Matheus Oliveria', Email='matheus@gmail.com',
               telefone='(84)98102-3323', situacao='Ativo',
               matricula='2138', turno_aula='Vespetino', cpf='800.400.220-01', dataNascimento='1992-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno9 = Aluno(username='2118', first_name='Thiago Silva', nome='Thiago Silva', Email='thiago@gmail.com',
               telefone='(84)91102-3323', situacao='Ativo',
               matricula='2118', turno_aula='Vespetino', cpf='900.400.220-01', dataNascimento='1995-02-22',
               endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno10 = Aluno(username='21197', first_name='Josival Xavier', nome='Josival Xavier', Email='josival@gmail.com',
                telefone='(84)94102-3323', situacao='Ativo',
                matricula='21197', turno_aula='Vespetino', cpf='110.400.202-01', dataNascimento='1992-02-22',
                endereco='Rua Bernando Viera, Natal - RN', sexo='Masculino')
aluno11 = Aluno(username='21090', first_name='Emilly Xavier', nome='Emilly Xavier', Email='emylli@gmail.com',
                telefone='(84)94102-3323', situacao='Ativo',
                matricula='21090', turno_aula='Vespetino', cpf='120.400.220-01', dataNascimento='1992-02-22',
                endereco='Rua Bernando Viera, Natal - RN', sexo='Feminino')
aluno.save()
aluno2.save()
aluno3.save()
aluno4.save()
aluno5.save()
aluno6.save()
aluno7.save()
aluno8.save()
aluno9.save()
aluno10.save()
aluno11.save()

grupoAluno = Group.objects.get(name='Aluno')
grupoAluno.user_set.add(aluno)
grupoAluno.user_set.add(aluno2)
grupoAluno.user_set.add(aluno3)
grupoAluno.user_set.add(aluno4)
grupoAluno.user_set.add(aluno5)
grupoAluno.user_set.add(aluno6)
grupoAluno.user_set.add(aluno7)
grupoAluno.user_set.add(aluno8)
grupoAluno.user_set.add(aluno9)
grupoAluno.user_set.add(aluno10)
grupoAluno.user_set.add(aluno11)

frequencia01 = Frequencia(data='2017-05-01',hora_entrada='08:10:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia02 = Frequencia(data='2017-05-02',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia03 = Frequencia(data='2017-05-03',hora_entrada='08:20:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia04 = Frequencia(data='2017-05-04',hora_entrada='08:50:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia05 = Frequencia(data='2017-05-05',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia06 = Frequencia(data='2017-05-08',hora_entrada='08:20:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia07 = Frequencia(data='2017-05-09',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia08 = Frequencia(data='2017-05-10',hora_entrada='08:10:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia09 = Frequencia(data='2017-05-11',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia10 = Frequencia(data='2017-05-12',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia11 = Frequencia(data='2017-05-15',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia12 = Frequencia(data='2017-05-16',hora_entrada='08:50:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia13 = Frequencia(data='2017-05-17',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia14 = Frequencia(data='2017-05-18',hora_entrada='08:20:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia15 = Frequencia(data='2017-05-19',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia16 = Frequencia(data='2017-05-22',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia17 = Frequencia(data='2017-05-23',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia18 = Frequencia(data='2017-05-24',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia19 = Frequencia(data='2017-05-25',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia20 = Frequencia(data='2017-05-26',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia21 = Frequencia(data='2017-05-29',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia22 = Frequencia(data='2017-05-30',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia23 = Frequencia(data='2017-05-31',hora_entrada='08:00:00',hora_saida='12:00:00',local="Laboratorio de informatica",pessoa=aluno)
frequencia24 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia25 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia26 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia27 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia28 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia29 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia30 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia31 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia32 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia33 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia34 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia35 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia36 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia37 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia38 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia39 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia40 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia41 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia42 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia43 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)
frequencia44 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno)

frequencia01.save()
frequencia02.save()
frequencia03.save()
frequencia04.save()
frequencia05.save()
frequencia06.save()
frequencia07.save()
frequencia08.save()
frequencia09.save()
frequencia10.save()
frequencia11.save()
frequencia12.save()
frequencia13.save()
frequencia14.save()
frequencia15.save()
frequencia16.save()
frequencia17.save()
frequencia18.save()
frequencia19.save()
frequencia20.save()
frequencia21.save()
frequencia22.save()
frequencia23.save()
frequencia24.save()
frequencia25.save()
frequencia26.save()
frequencia27.save()
frequencia28.save()
frequencia29.save()
frequencia30.save()
frequencia31.save()
frequencia32.save()
frequencia33.save()
frequencia34.save()
frequencia35.save()
frequencia36.save()
frequencia37.save()
frequencia38.save()
frequencia39.save()
frequencia40.save()
frequencia41.save()
frequencia42.save()
frequencia43.save()
frequencia44.save()

frequencia45 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia46 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia47 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia48 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia49 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia50 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia51 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia52 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia53 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia54 = Frequencia(data='2017-05-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia55 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia56 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia57 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia58 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia59 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia60 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia61 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia62 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia63 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia64 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia65 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia66 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia67 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia68 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia69 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia70 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia71 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia72 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia73 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia74 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia75 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia76 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia77 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia78 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia79 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia80 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia81 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia82 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia83 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia84 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia85 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia86 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia87 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)
frequencia88 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno2)

frequencia45.save()
frequencia46.save()
frequencia47.save()
frequencia48.save()
frequencia49.save()
frequencia50.save()
frequencia51.save()
frequencia52.save()
frequencia53.save()
frequencia54.save()
frequencia55.save()
frequencia56.save()
frequencia57.save()
frequencia58.save()
frequencia59.save()
frequencia60.save()
frequencia61.save()
frequencia62.save()
frequencia63.save()
frequencia64.save()
frequencia65.save()
frequencia66.save()
frequencia67.save()
frequencia68.save()
frequencia69.save()
frequencia70.save()
frequencia71.save()
frequencia72.save()
frequencia73.save()
frequencia74.save()
frequencia75.save()
frequencia76.save()
frequencia77.save()
frequencia78.save()
frequencia79.save()
frequencia80.save()
frequencia81.save()
frequencia82.save()
frequencia83.save()
frequencia84.save()
frequencia85.save()
frequencia86.save()
frequencia87.save()
frequencia88.save()

frequencia89 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia90 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia91 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia92 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia93 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia94 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia95 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia96 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia97 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia98 = Frequencia(data='2017-05-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia99 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                          local="Laboratorio de informatica", pessoa=aluno3)
frequencia100 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia101 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia102 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia103 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia104 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia105 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia106 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia107 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia108 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia109 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia110 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia111 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia112 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia113 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia114 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia115 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia116 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia117 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia118 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia119 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia120 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia121 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia122 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia123 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia124 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia125 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia126 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia127 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia128 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia129 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia130 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia131 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)
frequencia132 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratorio de informatica", pessoa=aluno3)

frequencia89.save()
frequencia90.save()
frequencia91.save()
frequencia92.save()
frequencia93.save()
frequencia94.save()
frequencia95.save()
frequencia96.save()
frequencia97.save()
frequencia98.save()
frequencia99.save()
frequencia100.save()
frequencia101.save()
frequencia102.save()
frequencia103.save()
frequencia104.save()
frequencia105.save()
frequencia106.save()
frequencia107.save()
frequencia108.save()
frequencia109.save()
frequencia110.save()
frequencia111.save()
frequencia112.save()
frequencia113.save()
frequencia114.save()
frequencia115.save()
frequencia116.save()
frequencia117.save()
frequencia118.save()
frequencia119.save()
frequencia120.save()
frequencia121.save()
frequencia122.save()
frequencia123.save()
frequencia124.save()
frequencia125.save()
frequencia126.save()
frequencia127.save()
frequencia128.save()
frequencia129.save()
frequencia130.save()
frequencia131.save()
frequencia132.save()

frequencia133 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia134 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia135 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia136 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia137 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia138 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia139 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia140 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia141 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia142 = Frequencia(data='2017-05-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia143 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia144 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia145 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia146 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia147 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia148 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia149 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia150 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia151 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia152 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia153 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia154 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia155 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia156 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia157 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia158 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia159 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia160 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia161 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia162 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia163 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia164 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia165 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia166 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia167 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia168 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia169 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia170 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia171 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia172 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia173 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia174 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia175 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)
frequencia176 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno4)

frequencia133.save()
frequencia134.save()
frequencia135.save()
frequencia136.save()
frequencia137.save()
frequencia138.save()
frequencia139.save()
frequencia140.save()
frequencia141.save()
frequencia142.save()
frequencia143.save()
frequencia144.save()
frequencia145.save()
frequencia146.save()
frequencia147.save()
frequencia148.save()
frequencia149.save()
frequencia150.save()
frequencia151.save()
frequencia152.save()
frequencia153.save()
frequencia154.save()
frequencia155.save()
frequencia156.save()
frequencia157.save()
frequencia158.save()
frequencia159.save()
frequencia160.save()
frequencia161.save()
frequencia162.save()
frequencia163.save()
frequencia164.save()
frequencia165.save()
frequencia166.save()
frequencia167.save()
frequencia168.save()
frequencia169.save()
frequencia170.save()
frequencia171.save()
frequencia172.save()
frequencia173.save()
frequencia174.save()
frequencia175.save()
frequencia176.save()

frequencia177 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia178 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia179 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia180 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia181 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia182 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia183 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia184 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia185 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia186 = Frequencia(data='2017-05-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia187 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia188 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia189 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia190 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia191 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia192 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia193 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia194 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia195 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia196 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia197 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia198 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia199 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia200 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia201 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia202 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia203 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia204 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia205 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia206 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia207 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia208 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia209 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia210 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia211 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia212 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia213 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia214 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia215 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia216 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia217 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia218 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia219 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)
frequencia220 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno11)

frequencia177.save()
frequencia178.save()
frequencia179.save()
frequencia180.save()
frequencia181.save()
frequencia182.save()
frequencia183.save()
frequencia184.save()
frequencia185.save()
frequencia186.save()
frequencia187.save()
frequencia188.save()
frequencia189.save()
frequencia190.save()
frequencia191.save()
frequencia192.save()
frequencia193.save()
frequencia194.save()
frequencia195.save()
frequencia196.save()
frequencia197.save()
frequencia198.save()
frequencia199.save()
frequencia200.save()
frequencia201.save()
frequencia202.save()
frequencia203.save()
frequencia204.save()
frequencia205.save()
frequencia206.save()
frequencia207.save()
frequencia208.save()
frequencia209.save()
frequencia210.save()
frequencia211.save()
frequencia212.save()
frequencia213.save()
frequencia214.save()
frequencia215.save()
frequencia216.save()
frequencia217.save()
frequencia218.save()
frequencia219.save()
frequencia220.save()

frequencia221 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia222 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia223 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia224 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia225 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia226 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia227 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia228 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia229 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia230 = Frequencia(data='2017-05-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia231 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia232 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia233 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia234 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia235 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia236 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia237 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia238 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia239 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia240 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia241 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia242 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia243 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia244 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia245 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia246 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia247 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia248 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia249 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia250 = Frequencia(data='2017-06-12', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia251 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia252 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia253 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia254 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia255 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia256 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia257 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia258 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia259 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia260 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia261 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia262 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia263 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)
frequencia264 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='12:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno5)

frequencia221.save()
frequencia222.save()
frequencia223.save()
frequencia224.save()
frequencia225.save()
frequencia226.save()
frequencia227.save()
frequencia228.save()
frequencia229.save()
frequencia230.save()
frequencia231.save()
frequencia232.save()
frequencia233.save()
frequencia234.save()
frequencia235.save()
frequencia236.save()
frequencia237.save()
frequencia238.save()
frequencia239.save()
frequencia240.save()
frequencia241.save()
frequencia242.save()
frequencia243.save()
frequencia244.save()
frequencia245.save()
frequencia246.save()
frequencia247.save()
frequencia248.save()
frequencia249.save()
frequencia250.save()
frequencia251.save()
frequencia252.save()
frequencia253.save()
frequencia254.save()
frequencia255.save()
frequencia256.save()
frequencia257.save()
frequencia258.save()
frequencia259.save()
frequencia260.save()
frequencia261.save()
frequencia262.save()
frequencia263.save()
frequencia264.save()

frequencia265 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia266 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia267 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia268 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia269 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia270 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia271 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia272 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia273 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia274 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia275 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia276 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia277 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia278 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia279 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia280 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia281 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia282 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia283 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia284 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia285 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia286 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia287 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia288 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia289 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia290 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia291 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia292 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia293 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia294 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia295 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia296 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia297 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia298 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia299 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia300 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia301 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia302 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia303 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia304 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia305 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia306 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia307 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)
frequencia308 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno6)

frequencia265.save()
frequencia266.save()
frequencia267.save()
frequencia268.save()
frequencia269.save()
frequencia270.save()
frequencia271.save()
frequencia272.save()
frequencia273.save()
frequencia274.save()
frequencia275.save()
frequencia276.save()
frequencia277.save()
frequencia278.save()
frequencia279.save()
frequencia280.save()
frequencia281.save()
frequencia282.save()
frequencia283.save()
frequencia284.save()
frequencia285.save()
frequencia286.save()
frequencia287.save()
frequencia288.save()
frequencia289.save()
frequencia290.save()
frequencia291.save()
frequencia292.save()
frequencia293.save()
frequencia294.save()
frequencia295.save()
frequencia296.save()
frequencia297.save()
frequencia298.save()
frequencia299.save()
frequencia300.save()
frequencia301.save()
frequencia302.save()
frequencia303.save()
frequencia304.save()
frequencia305.save()
frequencia306.save()
frequencia307.save()
frequencia308.save()

frequencia265 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia266 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia267 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia268 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia269 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia270 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia271 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia272 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia273 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia274 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia275 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia276 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia277 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia278 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia279 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia280 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia281 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia282 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia283 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia284 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia285 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia286 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia287 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia288 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia289 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia290 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia291 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia292 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia293 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia294 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia295 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia296 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia297 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia298 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia299 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia300 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia301 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia302 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia303 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia304 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia305 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia306 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia307 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)
frequencia308 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno7)

frequencia265.save()
frequencia266.save()
frequencia267.save()
frequencia268.save()
frequencia269.save()
frequencia270.save()
frequencia271.save()
frequencia272.save()
frequencia273.save()
frequencia274.save()
frequencia275.save()
frequencia276.save()
frequencia277.save()
frequencia278.save()
frequencia279.save()
frequencia280.save()
frequencia281.save()
frequencia282.save()
frequencia283.save()
frequencia284.save()
frequencia285.save()
frequencia286.save()
frequencia287.save()
frequencia288.save()
frequencia289.save()
frequencia290.save()
frequencia291.save()
frequencia292.save()
frequencia293.save()
frequencia294.save()
frequencia295.save()
frequencia296.save()
frequencia297.save()
frequencia298.save()
frequencia299.save()
frequencia300.save()
frequencia301.save()
frequencia302.save()
frequencia303.save()
frequencia304.save()
frequencia305.save()
frequencia306.save()
frequencia307.save()
frequencia308.save()

frequencia309 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia310 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia311 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia312 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia313 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia314 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia315 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia316 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia317 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia318 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia319 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia320 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia321 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia322 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia323 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia324 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia325 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia326 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia327 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia328 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia329 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia330 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia331 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia332 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia333 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia334 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia335 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia336 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia337 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia338 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia339 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia340 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia341 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia342 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia343 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia344 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia345 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia346 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia347 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia348 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia349 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia350 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia351 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)
frequencia352 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Mecatrônica", pessoa=aluno8)

frequencia309.save()
frequencia310.save()
frequencia311.save()
frequencia312.save()
frequencia313.save()
frequencia314.save()
frequencia315.save()
frequencia316.save()
frequencia317.save()
frequencia318.save()
frequencia319.save()
frequencia320.save()
frequencia321.save()
frequencia322.save()
frequencia323.save()
frequencia324.save()
frequencia325.save()
frequencia326.save()
frequencia327.save()
frequencia328.save()
frequencia329.save()
frequencia330.save()
frequencia331.save()
frequencia332.save()
frequencia333.save()
frequencia334.save()
frequencia335.save()
frequencia336.save()
frequencia337.save()
frequencia338.save()
frequencia339.save()
frequencia340.save()
frequencia341.save()
frequencia342.save()
frequencia343.save()
frequencia344.save()
frequencia345.save()
frequencia346.save()
frequencia347.save()
frequencia348.save()
frequencia349.save()
frequencia350.save()
frequencia351.save()
frequencia352.save()

frequencia353 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia354 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia355 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia356 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia357 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia358 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia359 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia360 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia361 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia362 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia363 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia364 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia365 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia366 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia367 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia368 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia369 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia370 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia371 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia372 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia373 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia374 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia375 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia376 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia377 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia378 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia379 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia380 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia381 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia382 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia383 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia384 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia385 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia386 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia387 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia388 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia389 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia390 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia391 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia392 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia393 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia394 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia395 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia396 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno9)
frequencia353.save()
frequencia354.save()
frequencia355.save()
frequencia356.save()
frequencia357.save()
frequencia358.save()
frequencia359.save()
frequencia360.save()
frequencia361.save()
frequencia362.save()
frequencia363.save()
frequencia364.save()
frequencia365.save()
frequencia366.save()
frequencia367.save()
frequencia368.save()
frequencia369.save()
frequencia370.save()
frequencia371.save()
frequencia372.save()
frequencia373.save()
frequencia374.save()
frequencia375.save()
frequencia376.save()
frequencia377.save()
frequencia378.save()
frequencia379.save()
frequencia380.save()
frequencia381.save()
frequencia382.save()
frequencia383.save()
frequencia384.save()
frequencia385.save()
frequencia386.save()
frequencia387.save()
frequencia388.save()
frequencia389.save()
frequencia390.save()
frequencia391.save()
frequencia392.save()
frequencia393.save()
frequencia394.save()
frequencia395.save()
frequencia396.save()

frequencia397 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia398 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia399 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia400 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia401 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia402 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia403 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia404 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia405 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia406 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia407 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia408 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia409 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia410 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia411 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia412 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia413 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia414 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia415 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia416 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia417 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia418 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia419 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia420 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia421 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia422 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia423 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia424 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia425 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia426 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia427 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia428 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia429 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia430 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia431 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia432 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia433 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia434 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia435 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia436 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia437 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia438 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia439 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)
frequencia440 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Laboratório de Eletrônica", pessoa=aluno10)

frequencia397.save()
frequencia398.save()
frequencia399.save()
frequencia400.save()
frequencia401.save()
frequencia402.save()
frequencia403.save()
frequencia404.save()
frequencia405.save()
frequencia406.save()
frequencia407.save()
frequencia408.save()
frequencia409.save()
frequencia410.save()
frequencia411.save()
frequencia412.save()
frequencia413.save()
frequencia414.save()
frequencia415.save()
frequencia416.save()
frequencia417.save()
frequencia418.save()
frequencia419.save()
frequencia420.save()
frequencia421.save()
frequencia422.save()
frequencia423.save()
frequencia424.save()
frequencia425.save()
frequencia426.save()
frequencia427.save()
frequencia428.save()
frequencia429.save()
frequencia430.save()
frequencia431.save()
frequencia432.save()
frequencia433.save()
frequencia434.save()
frequencia435.save()
frequencia436.save()
frequencia437.save()
frequencia438.save()
frequencia439.save()
frequencia440.save()
