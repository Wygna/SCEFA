from django.contrib.auth.models import Group

from appPonto.models import *

funcionarios=Group(name="Funcionarios")
funcionarios.save()
alunos=Group(name="Alunos")
alunos.save()
administradores=Group(name="Administradores")
administradores.save()

departamento = Departamento(descricao='Coordenação de Pesquisa')
departamento2 = Departamento(descricao='Coordenação de Cursos')

departamento.save()
departamento2.save()

cargo = Cargo(nome_funcao='Professor',departamento=departamento)
cargo2 = Cargo(nome_funcao='Administrador',departamento=departamento)
cargo3 = Cargo(nome_funcao='Coordenador',departamento=departamento)
cargo.save()
cargo2.save()
cargo3.save()

funcionario = Funcionario(username='225', cargo=cargo, first_name='Jose Antonio', nome='Jose Antonio', situacao='Ativo',
                          Email='jose@gmail.com', telefone='(84)99122-3323', matricula='225')
funcionario2 = Funcionario(username='2212', cargo=cargo2, first_name='Valerio Junior', nome='Valerio Junior',
                           situacao='Ativo',
                           Email='valerio@gmail.com', telefone='(84)99122-0000', matricula='2212')
funcionario3 = Funcionario(username='213', cargo=cargo, first_name='Marcos Calvacante', nome='Marcos Calvacante',
                           situacao='Ativo',
                           Email='marcos@gmail.com', telefone='(84)99100-3323', matricula='213')
funcionario4 = Funcionario(username='251', cargo=cargo, first_name='Fernanda Silva', nome='Fernanda Silva',
                           situacao='Ativo',
                           Email='fernanda@gmail.com', telefone='(84)98122-3323', matricula='251')
funcionario5 = Funcionario(username='259', cargo=cargo3, first_name='karol Soares', nome='Karol Soares',
                           situacao='Ativo',
                           Email='karol@gmail.com', telefone='(84)99122-3303', matricula='259')
funcionario6 = Funcionario(username='3225', cargo=cargo, first_name='Bruno Silva', nome='Bruno Silva', situacao='Ativo',
                           Email='Bruno@gmail.com', telefone='(84)93122-3323', matricula='3225')
funcionario7 = Funcionario(username='32212', cargo=cargo2, first_name='Marcelo Siqueira', nome='Marcelo Siqueira',
                           situacao='Ativo',
                           Email='marcelo@gmail.com', telefone='(84)99422-0000', matricula='32212')
funcionario8 = Funcionario(username='3213', cargo=cargo, first_name='Bento Oliveira', nome='Bento Oliveria',
                           situacao='Ativo',
                           Email='bento@gmail.com', telefone='(84)99130-3323', matricula='3213')
funcionario9 = Funcionario(username='3251', cargo=cargo, first_name='Ericka Lopes', nome='Ericka Lopes',
                           situacao='Ativo',
                           Email='ericka@gmail.com', telefone='(84)98152-3323', matricula='3251')
funcionario10 = Funcionario(username='3259', cargo=cargo, first_name='Joselha Oliveira', nome='Joselha Oliveira',
                            situacao='Ativo',
                            Email='joselha@gmail.com', telefone='(84)99342-3303', matricula='3259')
funcionario11 = Funcionario(username='30259', cargo=cargo, first_name='Neide Oliveira', nome='Neide Oliveira',
                            situacao='Ativo',
                            Email='neide@gmail.com', telefone='(84)98042-3303', matricula='30259')

funcionario.save()
funcionario2.save()
funcionario3.save()
funcionario4.save()
funcionario5.save()
funcionario6.save()
funcionario7.save()
funcionario8.save()
funcionario9.save()
funcionario10.save()
funcionario11.save()

grupofuncionario = Group.objects.get(name='Funcionarios')
grupofuncionario.user_set.add(funcionario)
grupofuncionario.user_set.add(funcionario3)
grupofuncionario.user_set.add(funcionario4)
grupofuncionario.user_set.add(funcionario5)
grupofuncionario.user_set.add(funcionario6)
grupofuncionario.user_set.add(funcionario7)
grupofuncionario.user_set.add(funcionario8)
grupofuncionario.user_set.add(funcionario9)
grupofuncionario.user_set.add(funcionario10)

grupoAdministrador = Group.objects.get(name='Administradores')
grupoAdministrador.user_set.add(funcionario2)
grupoAdministrador.user_set.add(funcionario11)

frequencia01 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia02 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia03 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia04 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia05 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia06 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia07 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia08 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia09 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia10 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia11 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia12 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia13 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia14 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia15 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia16 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia17 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia18 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia19 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia20 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia21 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia22 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia23 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia24 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia25 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia26 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia27 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia28 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia29 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia30 = Frequencia(data='2017-06-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia31 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia32 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia33 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia34 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia35 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia36 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia37 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia38 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia39 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia40 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia41 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia42 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia43 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)
frequencia44 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario)

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

frequencia45 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia46 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia47 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia48 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia49 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia50 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia51 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia52 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia53 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia54 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia55 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia56 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia57 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia58 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia59 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia60 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia61 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia62 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia63 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia64 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia65 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia66 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia67 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia68 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia69 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia70 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia71 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia72 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia73 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia74 = Frequencia(data='2017-06-17', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia75 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia76 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia77 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia78 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia79 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia80 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia81 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia82 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia83 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia84 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia85 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia86 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia87 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)
frequencia88 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='17:00:00',
                          local="Secretaria Acadêmica", pessoa=funcionario2)

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

frequencia89 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia90 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia91 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia92 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia93 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia94 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia95 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia96 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia97 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia98 = Frequencia(data='2017-05-18', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia99 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                          pessoa=funcionario3)
frequencia100 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia101 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia102 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia103 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia104 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia105 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia106 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia107 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia108 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia109 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia110 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia111 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia112 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia113 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia114 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia115 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia116 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia117 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia118 = Frequencia(data='2017-06-18', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia119 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia120 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia121 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia122 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia123 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia124 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia125 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia126 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia127 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia128 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia129 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia130 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia131 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)
frequencia132 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario3)

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

frequencia133 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia134 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia135 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia136 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia137 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia138 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia139 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia140 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia141 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia142 = Frequencia(data='2017-05-18', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia143 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia144 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia145 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia146 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia147 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia148 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia149 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia150 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia151 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia152 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia153 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia154 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia155 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia156 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia157 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia158 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia159 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia160 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia161 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia162 = Frequencia(data='2017-06-18', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia163 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia164 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia165 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia166 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia167 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia168 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia169 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia170 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia171 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia172 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia173 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia174 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia175 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)
frequencia176 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='18:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario4)

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

frequencia177 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia178 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia179 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia180 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia181 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia182 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia183 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia184 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia185 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia186 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia187 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia188 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia189 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia190 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia191 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia192 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia193 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia194 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia195 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia196 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia197 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia198 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia199 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia200 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia201 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia202 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia203 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia204 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia205 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia206 = Frequencia(data='2017-06-19', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia207 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia208 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia209 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia210 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia211 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia212 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia213 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia214 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia215 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia216 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia217 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia218 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia219 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)
frequencia220 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='19:00:00',
                           local="Sala de Recursos Humanos", pessoa=funcionario5)

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

frequencia221 = Frequencia(data='2017-05-01', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia222 = Frequencia(data='2017-05-02', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia223 = Frequencia(data='2017-05-03', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia224 = Frequencia(data='2017-05-04', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia225 = Frequencia(data='2017-05-05', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia226 = Frequencia(data='2017-05-08', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia227 = Frequencia(data='2017-05-09', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia228 = Frequencia(data='2017-05-10', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia229 = Frequencia(data='2017-05-11', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia230 = Frequencia(data='2017-05-18', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia231 = Frequencia(data='2017-05-15', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia232 = Frequencia(data='2017-05-16', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia233 = Frequencia(data='2017-05-17', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia234 = Frequencia(data='2017-05-18', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia235 = Frequencia(data='2017-05-19', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia236 = Frequencia(data='2017-05-22', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia237 = Frequencia(data='2017-05-23', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia238 = Frequencia(data='2017-05-24', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia239 = Frequencia(data='2017-05-25', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia240 = Frequencia(data='2017-05-26', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia241 = Frequencia(data='2017-05-29', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia242 = Frequencia(data='2017-05-30', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia243 = Frequencia(data='2017-05-31', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia244 = Frequencia(data='2017-06-01', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia245 = Frequencia(data='2017-06-02', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia246 = Frequencia(data='2017-06-05', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia247 = Frequencia(data='2017-06-06', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia248 = Frequencia(data='2017-06-07', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia249 = Frequencia(data='2017-06-09', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia250 = Frequencia(data='2017-06-18', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia251 = Frequencia(data='2017-06-13', hora_entrada='08:10:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia252 = Frequencia(data='2017-06-14', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia253 = Frequencia(data='2017-06-15', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia254 = Frequencia(data='2017-06-16', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia255 = Frequencia(data='2017-06-19', hora_entrada='08:50:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia256 = Frequencia(data='2017-06-20', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia257 = Frequencia(data='2017-06-21', hora_entrada='08:20:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia258 = Frequencia(data='2017-06-22', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia259 = Frequencia(data='2017-06-23', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia260 = Frequencia(data='2017-06-26', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia261 = Frequencia(data='2017-06-27', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia262 = Frequencia(data='2017-06-28', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia263 = Frequencia(data='2017-06-29', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)
frequencia264 = Frequencia(data='2017-06-30', hora_entrada='08:00:00', hora_saida='18:00:00', local="Sala de Pesquisa",
                           pessoa=funcionario6)

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

frequencia265 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia266 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia267 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia268 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia269 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia270 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia271 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia272 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia273 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia274 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia275 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia276 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia277 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia278 = Frequencia(data='2017-05-22', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia279 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia280 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia281 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia282 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia283 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia284 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia285 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia286 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia287 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia288 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia289 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia290 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia291 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia292 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia293 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia294 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia295 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia296 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia297 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia298 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia299 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia300 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia301 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia302 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia303 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia304 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia305 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia306 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia307 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)
frequencia308 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Coordenação de Cursos", pessoa=funcionario7)

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

frequencia265 = Frequencia(data='2017-05-01', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia266 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia267 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia268 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia269 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia270 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia271 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia272 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia273 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia274 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia275 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia276 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia277 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia278 = Frequencia(data='2017-05-22', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia279 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia280 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia281 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia282 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia283 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia284 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia285 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia286 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia287 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia288 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia289 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia290 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia291 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia292 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia293 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia294 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia295 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia296 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia297 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia298 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia299 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia300 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia301 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia302 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia303 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia304 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia305 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia306 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia307 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)
frequencia308 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='22:00:00',
                           local="Sala de Projeto de Extensão", pessoa=funcionario8)

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

frequencia309 = Frequencia(data='2017-05-01', hora_entrada='09:10:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia310 = Frequencia(data='2017-05-02', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia311 = Frequencia(data='2017-05-03', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia312 = Frequencia(data='2017-05-04', hora_entrada='09:50:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia313 = Frequencia(data='2017-05-05', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia314 = Frequencia(data='2017-05-09', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia315 = Frequencia(data='2017-05-09', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia316 = Frequencia(data='2017-05-10', hora_entrada='09:10:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia317 = Frequencia(data='2017-05-11', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia318 = Frequencia(data='2017-05-20', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia319 = Frequencia(data='2017-05-15', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia320 = Frequencia(data='2017-05-16', hora_entrada='09:50:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia321 = Frequencia(data='2017-05-17', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia322 = Frequencia(data='2017-05-20', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia323 = Frequencia(data='2017-05-19', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia324 = Frequencia(data='2017-05-22', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia325 = Frequencia(data='2017-05-23', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia326 = Frequencia(data='2017-05-24', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia327 = Frequencia(data='2017-05-25', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia328 = Frequencia(data='2017-05-26', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia329 = Frequencia(data='2017-05-29', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia330 = Frequencia(data='2017-05-30', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia331 = Frequencia(data='2017-05-31', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia332 = Frequencia(data='2017-06-01', hora_entrada='09:10:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia333 = Frequencia(data='2017-06-02', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia334 = Frequencia(data='2017-06-05', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia335 = Frequencia(data='2017-06-06', hora_entrada='09:50:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia336 = Frequencia(data='2017-06-07', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia337 = Frequencia(data='2017-06-09', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia338 = Frequencia(data='2017-06-20', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia339 = Frequencia(data='2017-06-09', hora_entrada='09:10:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia340 = Frequencia(data='2017-06-14', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia341 = Frequencia(data='2017-06-15', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia342 = Frequencia(data='2017-06-16', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia343 = Frequencia(data='2017-06-19', hora_entrada='09:50:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia344 = Frequencia(data='2017-06-20', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia345 = Frequencia(data='2017-06-21', hora_entrada='09:20:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia346 = Frequencia(data='2017-06-22', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia347 = Frequencia(data='2017-06-23', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia348 = Frequencia(data='2017-06-26', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia349 = Frequencia(data='2017-06-27', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia350 = Frequencia(data='2017-06-28', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia351 = Frequencia(data='2017-06-29', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)
frequencia352 = Frequencia(data='2017-06-30', hora_entrada='09:08:08', hora_saida='20:08:08',
                           local="Secretária Acadêmica", pessoa=funcionario9)

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
                           local="Assistência Social", pessoa=funcionario10)
frequencia354 = Frequencia(data='2017-05-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia355 = Frequencia(data='2017-05-03', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia356 = Frequencia(data='2017-05-04', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia357 = Frequencia(data='2017-05-05', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia358 = Frequencia(data='2017-05-13', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia359 = Frequencia(data='2017-05-09', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia360 = Frequencia(data='2017-05-10', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia361 = Frequencia(data='2017-05-11', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia362 = Frequencia(data='2017-05-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia363 = Frequencia(data='2017-05-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia364 = Frequencia(data='2017-05-16', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia365 = Frequencia(data='2017-05-17', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia366 = Frequencia(data='2017-05-18', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia367 = Frequencia(data='2017-05-19', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia368 = Frequencia(data='2017-05-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia369 = Frequencia(data='2017-05-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia370 = Frequencia(data='2017-05-24', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia371 = Frequencia(data='2017-05-25', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia372 = Frequencia(data='2017-05-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia373 = Frequencia(data='2017-05-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia374 = Frequencia(data='2017-05-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia375 = Frequencia(data='2017-05-31', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia376 = Frequencia(data='2017-06-01', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia377 = Frequencia(data='2017-06-02', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia378 = Frequencia(data='2017-06-05', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia379 = Frequencia(data='2017-06-06', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia380 = Frequencia(data='2017-06-07', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia381 = Frequencia(data='2017-06-09', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia382 = Frequencia(data='2017-06-18', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia383 = Frequencia(data='2017-06-13', hora_entrada='13:10:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia384 = Frequencia(data='2017-06-14', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia385 = Frequencia(data='2017-06-15', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia386 = Frequencia(data='2017-06-16', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia387 = Frequencia(data='2017-06-19', hora_entrada='13:50:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia388 = Frequencia(data='2017-06-20', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia389 = Frequencia(data='2017-06-21', hora_entrada='13:20:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia390 = Frequencia(data='2017-06-22', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia391 = Frequencia(data='2017-06-23', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia392 = Frequencia(data='2017-06-26', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia393 = Frequencia(data='2017-06-27', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia394 = Frequencia(data='2017-06-28', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia395 = Frequencia(data='2017-06-29', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
frequencia396 = Frequencia(data='2017-06-30', hora_entrada='13:00:00', hora_saida='18:00:00',
                           local="Assistência Social", pessoa=funcionario10)
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

frequencia397 = Frequencia(data='2017-05-01', hora_entrada='10:10:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia398 = Frequencia(data='2017-05-02', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia399 = Frequencia(data='2017-05-03', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia400 = Frequencia(data='2017-05-04', hora_entrada='10:50:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia401 = Frequencia(data='2017-05-05', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia402 = Frequencia(data='2017-05-10', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia403 = Frequencia(data='2017-05-09', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia404 = Frequencia(data='2017-05-10', hora_entrada='10:10:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia405 = Frequencia(data='2017-05-11', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia406 = Frequencia(data='2017-05-20', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia407 = Frequencia(data='2017-05-15', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia408 = Frequencia(data='2017-05-16', hora_entrada='10:50:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia409 = Frequencia(data='2017-05-17', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia410 = Frequencia(data='2017-05-20', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia411 = Frequencia(data='2017-05-19', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia412 = Frequencia(data='2017-05-22', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia413 = Frequencia(data='2017-05-23', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia414 = Frequencia(data='2017-05-24', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia415 = Frequencia(data='2017-05-25', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia416 = Frequencia(data='2017-05-26', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia417 = Frequencia(data='2017-05-29', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia418 = Frequencia(data='2017-05-30', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia419 = Frequencia(data='2017-05-31', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia420 = Frequencia(data='2017-06-01', hora_entrada='10:10:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia421 = Frequencia(data='2017-06-02', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia422 = Frequencia(data='2017-06-05', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia423 = Frequencia(data='2017-06-06', hora_entrada='10:50:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia424 = Frequencia(data='2017-06-07', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia425 = Frequencia(data='2017-06-09', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia426 = Frequencia(data='2017-06-20', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia427 = Frequencia(data='2017-06-10', hora_entrada='10:10:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia428 = Frequencia(data='2017-06-14', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia429 = Frequencia(data='2017-06-15', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia430 = Frequencia(data='2017-06-16', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia431 = Frequencia(data='2017-06-19', hora_entrada='10:50:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia432 = Frequencia(data='2017-06-20', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia433 = Frequencia(data='2017-06-21', hora_entrada='10:20:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia434 = Frequencia(data='2017-06-22', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia435 = Frequencia(data='2017-06-23', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia436 = Frequencia(data='2017-06-26', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia437 = Frequencia(data='2017-06-27', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia438 = Frequencia(data='2017-06-28', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia439 = Frequencia(data='2017-06-29', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)
frequencia440 = Frequencia(data='2017-06-30', hora_entrada='10:09:09', hora_saida='20:09:09', local="Apoio Acadêmico",
                           pessoa=funcionario11)

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
