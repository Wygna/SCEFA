from itertools import count
from django.contrib.auth.management import get_default_username
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models.aggregates import Max
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory
import datetime
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm
from appPonto.forms import *
from appPonto.models import *
from appPortas.models import Registro_porta
from django.db.models import Q
from appPonto.funcoes import *

@login_required(login_url='login')
def home(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def erro_permissao(request):
    return render(request,'utils/permissao.html')

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def funcionario_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(nome__icontains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(funcionarios,10)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios=paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados={'funcionarios':funcionarios,'criterio':criterio,'paginator':paginator,'page_obj':funcionarios}
    return render(request, 'Funcionario/funcionario_list.html',dados)

@permission_required('appPonto.delete_funcionario',login_url='erro_permissao')
def funcionario_delete(request,pk):
    try:
        funcionairo =Funcionario.objects.get(id=pk)
        funcionairo.delete()
        return redirect('funcionario_list')
    except Exception:
        mensagem ={'mensagem':'Não é possível excluir funcionario, excluir o funcionario selecionado exigiria excluir as frequências registradas'}
        return render(request,'utils/pagina_erro.html',mensagem)

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
            grupoFuncionario = Group.objects.get(name='Funcionarios')
            grupoFuncionario.user_set.add(funcionario)
            funcionario.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
        dados={'form':form}
        return render(request,'Funcionario/funcionario_form.html',dados)

@permission_required('appPonto.change_funcionario',login_url='erro_permissao')
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
        dados = {'form': form,'aluno':funcionario}
        return render(request, 'Funcionario/funcionario_form.html', dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def departamento_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        departamentos = Departamento.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        departamentos = Departamento.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(departamentos,10)
    page = request.GET.get('page')
    try:
        departamentos = paginator.page(page)
    except PageNotAnInteger:
        departamentos=paginator.page(1)
    except EmptyPage:
        departamentos = paginator.page(paginator.num_pages)
    dados={'departamentos':departamentos,'criterio':criterio,'paginator':paginator,'page_obj':departamentos}
    return render(request, 'Departamento/departamento_list.html', dados)

@permission_required('appPonto.view_departamento',login_url='erro_permissao')
def departamento_detail(request,pk):
    criterio = request.GET.get('criterio')
    departamento = Departamento.objects.get(id=pk)
    if criterio:
        cargos = Cargo.objects.filter(departamento=departamento,nome_funcao__icontains=criterio).order_by('nome_funcao')
    else:
        cargos = Cargo.objects.filter(departamento=departamento).order_by('nome_funcao')
        criterio = ""
    paginator = Paginator(cargos, 10)
    page = request.GET.get('page')
    try:
        cargos = paginator.page(page)
    except PageNotAnInteger:
        cargos = paginator.page(1)
    except EmptyPage:
        cargos = paginator.page(paginator.num_pages)
    dados = {'cargos': cargos, 'criterio': criterio, 'paginator': paginator, 'page_obj': cargos,'departamento':departamento}
    return render(request,'Departamento/exibirDepartamento.html',dados)

@permission_required('appPonto.add_departamento',login_url='erro_permissao')
def departamento_new(request):
    if (request.method == 'POST'):
        form = DepartamentoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('departamento_list')
    else:
        form=DepartamentoForm()
        dados={'form':form}
        return render(request, 'Departamento/departamento_form.html', dados)

@permission_required('appPonto.change_departamento',login_url='erro_permissao')
def departamento_update(request,pk):
    departamento = Departamento.objects.get(id=pk)
    if(request.method=='POST'):
        form=DepartamentoForm(request.POST,instance=departamento)
        if (form.is_valid()):
            form.save()
            return redirect('departamento_list')
    else:
        form = DepartamentoForm(instance=departamento)
        dados = {'form': form,'departamento':departamento}
        return render(request, 'Departamento/departamento_form.html', dados)

@permission_required('appPonto.delete_departamento', login_url='erro_permissao')
def departamento_delete(request,pk):
    try:
        departamento =Departamento.objects.get(id=pk)
        departamento.delete()
        return redirect('departamento_list')
    except Exception:
        mensagem = {'mensagem': 'Não é possível excluir departamento, o departamento selecionado está relacionado a um cargo'}
        return render(request, 'utils/pagina_erro.html', mensagem)


@permission_required('appPonto.view_cargo',login_url='erro_permissao')
def cargo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        cargos = Cargo.objects.filter(nome_funcao__icontains=criterio).order_by('nome_funcao')
    else:
        cargos = Cargo.objects.all().order_by('nome_funcao')
        cargos = Cargo.objects.filter()
        criterio =""
    paginator =Paginator(cargos,10)
    page = request.GET.get('page')
    try:
        cargos = paginator.page(page)
    except PageNotAnInteger:
        cargos=paginator.page(1)
    except EmptyPage:
        cargos = paginator.page(paginator.num_pages)
    dados={'cargos':cargos,'criterio':criterio,'paginator':paginator,'page_obj':cargos}
    return render(request, 'Cargo/cargo_list.html', dados)

@permission_required('appPonto.view_cargo',login_url='erro_permissao')
def cargo_detail(request,pk):
    cargo = Cargo.objects.get(id=pk)
    departamento = Departamento.objects.get(id=cargo.departamento.id)
    funcionarios = Funcionario.objects.filter(cargo=cargo)
    return render(request,'Cargo/exibirCargo.html',{'cargo':cargo,'funcionarios':funcionarios,'departamento':departamento})

@permission_required('appPonto.add_cargo',login_url='erro_permissao')
def cargo_new(request):
    if (request.method == 'POST'):
        form = CargoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form=CargoForm()
        dados={'form':form}
        return render(request, 'Cargo/cargo_form.html', dados)

@permission_required('appPonto.change_cargo',login_url='erro_permissao')
def cargo_update(request,pk):
    cargo = Cargo.objects.get(id=pk)
    if(request.method=='POST'):
        form=CargoForm(request.POST,instance=cargo)
        if (form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm(instance=cargo)
        dados = {'form': form,'cargo':cargo}
        return render(request, 'Cargo/cargo_form.html', dados)

@permission_required('appPonto.delete_departamento', login_url='erro_permissao')
def cargo_delete(request,pk):
    cargo =Cargo.objects.get(id=pk)
    cargo.delete()
    return redirect('cargo_list')

@permission_required('appPonto.change_funcionario',login_url='erro_permissao')
def funcionairo_administrardor_update(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    if request.method =="POST":
        form =FuncionarioForm(request.POST,instance=funcionario)
        if form.is_valid():
            funcionario = form.save()
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            funcionario.set_password(funcionario.senha)
            grupoFuncionario = Group.objects.get(name='Funcionarios')
            grupoFuncionario.user_set.add(funcionario)
            funcionario.save()
            return redirect('administrador_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {'form': form,'aluno':funcionario}
        return render(request, 'Funcionario/funcionario_form.html', dados)


@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def administrador_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        administradores = Funcionario.objects.filter(cargo__nome_funcao='Administrador',nome__icontains=criterio).order_by('nome')
    else:
        administradores = Funcionario.objects.filter(cargo__nome_funcao='Administrador').order_by('nome')
        criterio =""
    paginator =Paginator(administradores,4)
    page = request.GET.get('page')
    try:
        administradores = paginator.page(page)
    except PageNotAnInteger:
        administradores=paginator.page(1)
    except EmptyPage:
        administradores = paginator.page(paginator.num_pages)
    dados={'administradores':administradores,'criterio':criterio,'paginator':paginator,'page_obj':administradores}
    return render(request, 'Administrador/administrador_list.html',dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def funcionarios_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(nome__icontains=criterio).order_by('nome')
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
    return render(request, 'Frequencia/frequencia_funcionario_list.html', dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def administrador_new(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.filter(~Q(cargo__nome_funcao__contains='Administrador'))
        criterio = ""
    paginator = Paginator(funcionarios, 4)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados = {'funcionarios': funcionarios, 'criterio': criterio, 'paginator': paginator, 'page_obj': funcionarios}
    return render(request, 'Administrador/administrador_form.html', dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def adicionar_administrador(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    grupoAdministrador = Group.objects.get(name='Administradores')
    grupoFuncionario = Group.objects.get(name='Funcionarios')
    grupoFuncionario.user_set.remove(funcionario)
    grupoAdministrador.user_set.add(funcionario)
    funcionario.setCargo('Administrador')
    funcionario.save()
    return redirect('administrador_new')

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def remover_administrador(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    grupoAdministrador = Group.objects.get(name='Administradores')
    grupoFuncionario = Group.objects.get(name='Funcionarios')
    grupoAdministrador.user_set.remove(funcionario)
    grupoFuncionario.user_set.add(funcionario)
    funcionario.setCargo('Professor')
    funcionario.save()
    return redirect('administrador_list')

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def funcionario_frequencia(request,pk):
    current_user = request.user
    try:
        funcionario = Funcionario.objects.get(id=pk)
        if funcionario.matricula ==  current_user.username:
            data_inicial = request.GET.get('data_inicial')
            data_final = request.GET.get('data_final')
            if validar_data(data_inicial) and validar_data(data_final):
                data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
                data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")

                frequencias = funcionario.frequencia_set.filter(~Q(data__week_day=7),~Q(data__week_day=1),data__gte=data_inicial_formatada,data__lte=data_final_formatada).order_by('data')
                frequencia_com_expediente = []
                for frequencia in frequencias:
                    if frequencia.data not in datas_sem_expediente():
                        frequencia_com_expediente.append(frequencia)
                dias_trabalhados = dias_registrados(frequencia_com_expediente)
                dias_nao_trabalhados = dias_nao_registrados(frequencia_com_expediente)
                horas_total = tempo_total(frequencia_com_expediente)
                dados = {'frequencias':frequencia_com_expediente,'funcionario':funcionario,'data_inicial':data_inicial,
                         'data_final':data_final,'dias_trabalhos':dias_trabalhados,'dias_nao_trabalhos':dias_nao_trabalhados,'horas_total':horas_total}
                return render(request, 'Frequencia/exibir_frequencia_funcionario.html', dados)
        else:
            return render(request,'utils/permissao.html')
    except Exception:
        mensagem = {
            'mensagem': 'Funcionario não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)


@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def funcionario_busca_frequencia(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    return render(request, 'Frequencia/busca_frequencia.html', {'funcionario':funcionario})