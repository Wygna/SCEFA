from django.db import models

# Create your models here.



class Porta(models.Model):
    descricao = models.CharField('Descrição', max_length=255)

    def __str__(self):
        return self.descricao
    class Meta: permissions = (('view_porta', 'Can see porta'),)

