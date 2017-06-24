from appPonto.models import *

pessoa = Pessoa.objects.get(nome__icontains="Bruno Silva")
pessoa2 = Pessoa.objects.get(nome__icontains="Valerio Junior")
pessoa3 = Pessoa.objects.get(nome__icontains="Jose Antonio")
pessoa4 = Pessoa.objects.get(nome__icontains="Joselha Oliveira")
pessoa5 = Pessoa.objects.get(nome__icontains="Neide Oliveira")
pessoa6 = Pessoa.objects.get(nome__icontains="Marcelo Siqueira")
pessoa7 = Pessoa.objects.get(nome__icontains="Luiz Felipe")
pessoa8 = Pessoa.objects.get(nome__icontains="Paulo Cesar")
pessoa9 = Pessoa.objects.get(nome__icontains="Wallysson Lima")
pessoa10 = Pessoa.objects.get(nome__icontains="Juliana Soares")
pessoa11 = Pessoa.objects.get(nome__icontains="Lucas Lima")
