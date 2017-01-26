from django.contrib.auth.management import get_default_username
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory
import datetime as DT
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm
from appPonto.forms import *
from appPonto.models import *


@login_required(login_url='login')
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def erro_permissao(request):
    return render(request,'utils/permissao.html')

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
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

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def funcionario_detail(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    return render(request,'Funcionario/exibirFuncionario.html',{'funcionario':funcionario})

@permission_required('appPonto.add_funcionario',login_url='erro_permissao')
def funcionario_new(request):
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST)
        if(form.is_valid()):
            funcionario = form.save()
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            funcionario.set_password(funcionario.senha)
            grupoFuncionario = Group.objects.get(name='funcionario')
            grupoFuncionario.user_set.add(funcionario)
            funcionario.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
        dados={'form':form}
        return render(request,'Funcionario/funcionario_form.html',dados)

@permission_required('appPonto.update_funcionario',login_url='erro_permissao')
def funcionairo_update(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    if request.method =="POST":
        form =FuncionarioForm(request.POST,instance=funcionario)
        if form.is_valid():
            funcionario = form.save()
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            funcionario.set_password(funcionario.senha)
            grupoFuncionario = Group.objects.get(name='funcionario')
            grupoFuncionario.user_set.add(funcionario)
            funcionario.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {'form': form,'funcionario':funcionario}
        return render(request, 'Funcionario/funcionario_form.html', dados)

@permission_required('appPonto.delete_funcionario',login_url='erro_permissao')
def funcionario_delete(request,pk):
    funcionairo =Funcionario.objects.get(id=pk)
    funcionairo.delete()
    return redirect('funcionario_list')

@permission_required('appPonto.view_administrador',login_url='erro_permissao')
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


def registroPonto_list(request):
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
    return render(request, 'RegistroPonto/RegistroPonto_list.html',dados)


@permission_required('appPonto.view_registroPonto',login_url='erro_permissao')
def registroPonto_list2(request):
    criterio = request.GET.get('criterio')
    if criterio:
        registroPonto = RegistrarPonto.objects.filter(nome__contains=criterio).order_by('local')
    else:
        registroPonto = RegistrarPonto.objects.all().order_by('local')
        criterio =""
    paginator =Paginator(registroPonto,100)
    page = request.GET.get('page')
    try:
        registroPonto = paginator.page(page)
    except PageNotAnInteger:
        registroPonto=paginator.page(1)
    except EmptyPage:
        registroPonto = paginator.page(paginator.num_pages)
    dados={'registroPontos':registroPonto,'criterio':criterio,'paginator':paginator,'page_obj':registroPonto}
    return render(request, 'RegistroPonto/RegistroPonto_list.html',dados)

@permission_required('appPonto.view_administrador',login_url='erro_permissao')
def administrador_detail(request,pk):
    administrador = Administrador.objects.get(id=pk)
    return render(request,'Administrador/exibirAdministrador.html',{'administrador':administrador})

@permission_required('appPonto.add_administrador',login_url='erro_permissao')
def administrador_new(request):
    if request.method=="POST":
        form = AdministradorForm(request.POST)
        if form.is_valid():
            administrador = form.save()
            administrador.username = administrador.matricula
            administrador.first_name = administrador.nome
            administrador.set_password(administrador.senha)
            grupoAdministrador = Group.objects.get(name='administrador')
            grupoAdministrador.user_set.add(administrador)
            administrador.save()
            return redirect('administrador_list')

    else:
        form = AdministradorForm
        dados = {'form':form}
        return render(request,'Administrador/administrador_form.html',dados)

@permission_required('appPonto.update_administrador',login_url='erro_permissao')
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

@permission_required('appPonto.delete_administrador',login_url='erro_permissao')
def administrador_delete(request,pk):
    administrador =Administrador.objects.get(id=pk)
    administrador.delete()
    return redirect('administrador_list')

@permission_required('appPonto.view_relatorio',login_url='erro_permissao')
def funcionario_relatorio(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    registroPonto = funcionario.registrarponto_set.all()
    return render(request,'RegistroPonto/exibirRegistroPontoFuncionario.html',{'registroPontos':registroPonto})