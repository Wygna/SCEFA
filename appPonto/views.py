from django.conf.locale import id
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields import Empty
from django.shortcuts import render, redirect

# Create your views here.
from appPonto.forms import FuncionarioForm, AdministradorForm
from appPonto.models import *


def home(request):
    return render(request,'base.html')

def funcionario_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(funcionarios,4)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios=paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados={'funcionarios':funcionarios,'criterio':criterio,'paginator':paginator,'page_obj':funcionarios}
    return render(request, 'Funcionario/funcionario_list.html',dados)

def funcionario_detail(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    return render(request,'Funcionario/exibirFuncionario.html',{'funcionairo':funcionario})

def funcionario_new(request):
    if request.method=="POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm
        dados = {'form':form}
        return render(request,'Funcionario/funcionario_form.html',dados)

def funcionairo_update(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    if request.method =="POST":
        form =FuncionarioForm(request.POST,instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {'form': form,'funcionario':funcionario}
        return render(request, 'Funcionario/funcionario_form.html', dados)

def funcionario_delete(request,pk):
    funcionairo =Funcionario.objects.get(id=pk)
    funcionairo.delete()
    return redirect('funcionario_list')

def administrador_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        administrador = Administrador.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        administrador = Administrador.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(administrador,4)
    page = request.GET.get('page')
    try:
        administrador = paginator.page(page)
    except PageNotAnInteger:
        administrador=paginator.page(1)
    except EmptyPage:
        administrador = paginator.page(paginator.num_pages)
    dados={'administradores':administrador,'criterio':criterio,'paginator':paginator,'page_obj':administrador}
    return render(request, 'Administrador/administrador_list.html',dados)

def administrador_detail(request,pk):
    administrador = Administrador.objects.get(id=pk)
    return render(request,'Administrador/exibirAdministrador.html',{'administrador':administrador})

def administrador_new(request):
    if request.method=="POST":
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador_list')
    else:
        form = AdministradorForm
        dados = {'form':form}
        return render(request,'Administrador/administrador_form.html',dados)

def administrador_update(request,pk):
    administrador = Administrador.objects.get(id=pk)
    if request.method =="POST":
        form =AdministradorForm(request.POST,instance=administrador)
        if form.is_valid():
            form.save()
            return redirect('administrador_list')
    else:
        form = AdministradorForm(instance=administrador)
        dados = {'form': form,'administrador':administrador}
        return render(request, 'Administrador/administrador_form.html', dados)

def administrador_delete(request,pk):
    administrador =Administrador.objects.get(id=pk)
    administrador.delete()
    return redirect('administrador_list')