from appPonto.models import *
from appPortas.models import *
from datetime import datetime

def conultar_pessoa_acesso_porta(id_digital, id_porta, img_digital):
    try:
        pessoagrupo = GrupoPessoa.objects.filter(pessoa__id_digital=id_digital)
        portagrupo = GrupoPorta.objects.filter(porta_id=id_porta)
    except GrupoPessoa.DoesNotExist:
        return False
    except GrupoPorta.DoesNotExist:
        return False
    acesso = False
    for pessoa in pessoagrupo:
        for porta in portagrupo:
            if pessoa.id == porta.id:
                acesso = True
    return acesso

def registra_acesso_porta(id_digital, id_porta, img_digital):
    hora = datetime.now()
    if conultar_pessoa_acesso_porta(id_digital, id_porta) == True:
        pessoa = Pessoa.objects.get(id_digital=id_digital)
        porta = Porta.objects.get(id=id_porta)
        registro_acesso = RegistroPorta.objects.create(data=datetime.now().date(),
                                                       hora_acesso=hora.strftime("%H:%M:%S"), porta=porta,
                                                       pessoa=pessoa)
        registro_acesso.save()
        return True
    else:
        return False

def registra_frequencia_entrada(id_digital, img_digital, local):
    hora = datetime.now()
    try:
        pessoa = Pessoa.objects.get(id_digital=id_digital)
    except Pessoa.DoesNotExist:
        return False
    frequencia = Frequencia.objects.create(data=datetime.now().date(), hora_entrada=hora.strftime("%H:%M:%S"),
                                           hora_saida=None, pessoa=pessoa, local=local)
    frequencia.save()
    return True

def registra_frequencia_saida(id_digital, img_digital, local):
    hora = datetime.now()
    try:
        frequencia = Frequencia.objects.get(pessoa__id_digital=id_digital, data=datetime.now().date())
    except Pessoa.DoesNotExist:
        return False
    frequencia.hora_saida = hora.strftime("%H:%M:%S")
    frequencia.local = local
    frequencia.save()
    return True


def adicionar_biometria(id_digital, img_digital, matricula):
    try:
        pessoa = Pessoa.objects.get(username=matricula)
    except Pessoa.DoesNotExist:
        return False
    pessoa.id_digital = id_digital
    pessoa.img_dital = img_digital
    pessoa.save()
    return True
