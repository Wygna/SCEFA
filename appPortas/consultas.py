from django.contrib.gis.utils.wkt import precision_wkt

from appPonto.models import *
from appPortas.models import *
from datetime import datetime


def consultar_pessoa_acesso_porta(id_digital, id_porta, img_digital):
    try:
        grupopessoa = GrupoPessoa.objects.filter(pessoa__id_digital=id_digital)
        grupoporta = GrupoPorta.objects.filter(porta_id=id_porta)
    except GrupoPessoa.DoesNotExist:
        return False
    except GrupoPorta.DoesNotExist:
        return False
    acesso = False
    for grupo in grupopessoa:
        for porta in grupoporta:
            if grupo.grupo == porta.grupo:
                acesso = True
    return acesso


def registra_acesso_porta(id_digital, id_porta, img_digital):
    hora = datetime.now()
    if consultar_pessoa_acesso_porta(id_digital, id_porta, img_digital) == (True):
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
    not_frequencia = True
    try:
        Frequencia.objects.get(pessoa__id_digital=32, data=datetime.now().date())
        not_frequencia = False
    except Frequencia.DoesNotExist:
        not_frequencia = True
    hora = datetime.now()

    if not_frequencia:
        try:
            pessoa = Pessoa.objects.get(id_digital=id_digital)
        except Pessoa.DoesNotExist:
            return False
        frequencia = Frequencia.objects.create(data=datetime.now().date(), hora_entrada=hora.strftime("%H:%M:%S"),
                                               hora_saida=None, pessoa=pessoa, local=local)
        frequencia.save()
        return True
    else:
        return False


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


print(adicionar_biometria(88, 'img', 251))
