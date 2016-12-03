from django.db import models

class Pessoa(models.Model):
    nome = models.CharField("Nome",max_length=255)
    email = models.EmailField("E-mail",max_length=200)
    telefone = models.CharField("Telefone",max_length=20)
    matricula = models.CharField("Matricula",max_length=10,unique=True)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    enderecao = models.CharField("Endereço",max_length=255)

class Administrador(Pessoa):
    enderecao = models.CharField("Endereço",max_length=255)
