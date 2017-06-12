from appPonto.models import *

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