import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
class Pessoa(User):
    nome = models.CharField("Nome", max_length=255)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    sexos = (('Masculino', 'Masculino'),
             ('Feminino', 'Feminino'),)
    sexo = models.CharField(max_length=30, choices=sexos)
    Email = models.EmailField("E-mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    dataNascimento = models.DateField('Data de Nascimento', max_length=10)
    endereco = models.CharField('Endereço', max_length=200, null=True)
    id_digital = models.IntegerField(null=True, blank=True, unique=True)
    img_dital = models.CharField(null=True, max_length=100, blank=True)
    Situacoes = (
        ('Ativo', 'Ativo'),
        ('Desativado', 'Desativado'),
    )
    situacao = models.CharField('Situação',
                                max_length=30,
                                choices=Situacoes,
                                )
    foto = models.ImageField(
        upload_to='fotos', verbose_name='foto',
        null=True, blank=True)

    def __str__(self):
        return self.nome
    class Meta: permissions = (('view_pessoa', 'Can see pessoa'),)

class Departamento(models.Model):
    descricao = models.CharField("Descrição",max_length=200)
    class Meta: permissions = (('view_departamento', 'Can see departamento'),)
    def __str__(self):
        return self.descricao

class Cargo(models.Model):
    nome_funcao = models.CharField('Nome da função',max_length=200)
    departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT,verbose_name="Departamento")
    class Meta: permissions = (('view_cargo', 'Can see cargo'),)
    def __str__(self):
        return self.nome_funcao

class Funcionario(Pessoa):
    matricula = models.CharField("Matricula", max_length=20, unique=True)
    cargo = models.ForeignKey(Cargo,on_delete=models.PROTECT,verbose_name="Cargo")
    dataAdmissao = models.DateField('Data de Admissão', default=timezone.now)
    salario = models.DecimalField("Salário", max_digits=10, decimal_places=2, null=True)

    def setCargo(self,funcao):
        cargo = Cargo.objects.get(nome_funcao=funcao)
        self.cargo = cargo

    def __str__(self):
        return self.nome
    class Meta: permissions = (('view_funcionario', 'Can see funcionario'),)

class Frequencia(models.Model):
    data = models.DateField(default=timezone.now)
    hora_entrada = models.TimeField(default=timezone.now,null=True)
    hora_saida = models.TimeField(default=timezone.now,null=True)
    local = models.CharField("local",max_length=200,null=True)
    observacao = models.CharField("Observação",max_length=200,null=True)
    pessoa = models.ForeignKey(Pessoa,on_delete=models.PROTECT)
    inconsistencia = models.BooleanField(default=False)
    arquivo = models.FileField(upload_to='arquivos', verbose_name='arquivo', null=True, blank=True)

    def TotalEntradaSaida(self):
        if self.hora_entrada !=None:
            formatacao = '%H:%M:%S'
            hora = datetime.datetime.strptime(str(self.hora_saida), formatacao) - datetime.datetime.strptime(str(self.hora_entrada), formatacao)
            return hora
        else:
            return "0:00:00"

    def tempoMaximo(self):
        formatacao = '%H:%M:%S'
        if self.hora_entrada == None or self.hora_saida == None:
            return 0
        else:
            tempo = str(datetime.datetime.strptime(str(self.hora_saida), formatacao) - datetime.datetime.strptime(
                str(self.hora_entrada), formatacao))
            if tempo[1] != ':':
                tempo_maximo = datetime.time(int(tempo[0:2]), int(tempo[3:5], int(tempo[6:])))
                if tempo_maximo > datetime.time(10, 0, 1):
                    return 1
            else:
                return 0

    def diaSemana(self):
        semana= ['Segunda-Feira', 'Terceira-Feira', 'Quarta-Feira',
        'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return semana[self.data.weekday()]

    def __str__(self):
        return str(self.data.isoformat())+" "+str(self.pessoa)

    @classmethod
    def tempoTotal(cls, frequencias):
        segundos = 0
        formatacao = '%H:%M:%S'
        for frequencia in frequencias:
            if frequencia.hora_saida == None:
                continue
            segundos += (
                datetime.datetime.strptime(str(frequencia.hora_saida), formatacao) - datetime.datetime.strptime(
                    str(frequencia.hora_entrada),
                    formatacao)).seconds
        horas = segundos / 3600
        min = (segundos % 3600) / 60
        sec = segundos % 60
        tempo = "%d:%d:%d" % (horas, min, sec)
        return tempo

    @classmethod
    def validarData(cls, data):
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

    @classmethod
    def quantidadePresenca(cls, frequencias):
        quantidade_dias = 0
        for frequencia in frequencias:
            if frequencia.inconsistencia == False:
                quantidade_dias += 1
        return quantidade_dias

    @classmethod
    def quantidadeFaltas(cls, frequencias):
        quantidade_dias = 0
        for frequencia in frequencias:
            if frequencia.inconsistencia == True:
                quantidade_dias += 1
        return quantidade_dias

    @classmethod
    def frequencias(cls, data_inicial, data_final, pessoa):
        frequencias = pessoa.frequencia_set.filter(~Q(data__week_day=7), ~Q(data__week_day=1), data__gte=data_inicial,
                                                   data__lte=data_final).order_by('data')
        frequencia_com_expediente = []
        for frequencia in frequencias:
            if frequencia.data not in DiasSemExpediente.datasSemExpediente():
                frequencia_com_expediente.append(frequencia)
        return frequencia_com_expediente

    class Meta: permissions = (('view_frequencia', 'Can see frequencia'),
                                   ('view_frequencia_admin', 'Can see frequencia a mais'),)

class DiasSemExpediente(models.Model):
    data = models.DateField('Data', max_length=10)
    descricao = models.CharField("Descrição",max_length=200,null=True)

    @classmethod
    def datasSemExpediente(cls):
        datas = []
        for data in DiasSemExpediente.objects.all():
            datas.append(data)
        return datas

    def __str__(self):
        return self.data.isoformat()

    class Meta: permissions = (('view_diasSemExpediente', 'Can see dias sem expediente'),)

class Horario(models.Model):
    cargahoraria = models.IntegerField('Carga horária')
    DIAS_SEMANA = (
        ('Segunda-Feira', 'Segunda-Feira'),
        ('Terça-Feira', 'Terça-Feira'),
        ('Quarta-Feira', 'Quarta-Feira'),
        ('Quinta-Feira', 'Quinta-Feira'),
        ('Sexta-Feira', 'Sexta-Feira'),
        ('Sábado', 'Sábado'),
    )
    dias = MultiSelectField(choices=DIAS_SEMANA, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    class Meta: permissions = (('view_horario', 'Can see horario'),)
