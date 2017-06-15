from django.db.models import Q
from appPonto.models import *
import datetime

def validar_data(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    validade = "true"
    i = 0
    while validade == "true" and i == 0:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            bissexto = "sim"
        else:
            bissexto = "nao"
        if mes < 1 or mes > 12:
            validade = "false"
        if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
            validade = "false"
        if (mes == 2 and bissexto == "nao" and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
            validade = "false"
        i = i + 1
    if validade == "true":
        return True
    else:
        return False

def datas_sem_expediente():
    dias_sem_expediente = Dias_sem_expediente.objects.all()
    datas = []
    for data in dias_sem_expediente:
        datas.append(data.data)
    return datas
def dias_registrados(frequencia_com_expediente):
    quantidade_dias = 0
    for frequencia in frequencia_com_expediente:
        if frequencia.hora_entrada != None:
            quantidade_dias+=1
    return quantidade_dias

def dias_nao_registrados(frequencia_com_expediente):
    quantidade_dias = 0
    for frequencia in frequencia_com_expediente:
        if frequencia.hora_entrada == None or frequencia.hora_saida == None:
            quantidade_dias+=1
    return quantidade_dias
def tempo_total(frequencias):
    segundos = 0
    formatacao = '%H:%M:%S'
    for frequencia in frequencias:
        if frequencia.hora_saida ==None:
            continue
        segundos += (datetime.datetime.strptime(str(frequencia.hora_saida), formatacao) - datetime.datetime.strptime(
            str(frequencia.hora_entrada),
            formatacao)).seconds
    horas = segundos / 3600
    min = (segundos % 3600) / 60
    sec = segundos % 60
    tempo = "%d:%d:%d" % (horas, min, sec)
    return tempo
