from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from appPonto.forms import *
from appPortas.models import *

@login_required(login_url='login')
def home(request):
    dados = {}
    id_pessoa = request.user.id
    if not request.user.is_superuser:
        pessoa = Pessoa.objects.get(id=id_pessoa)
        grupos = GrupoPessoa.objects.filter(pessoa=pessoa)
        dados = {'grupos': grupos}
    return render(request, 'index.html', dados)

@login_required(login_url='login')
def erro_permissao(request):
    return render(request,'utils/permissao.html')

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def funcionario_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(~Q(cargo__nome_funcao__contains='Administrador'),
                                                  nome__icontains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.filter(~Q(cargo__nome_funcao__contains='Administrador')).order_by('nome')
        criterio =""
    paginator = Paginator(funcionarios, 8)
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
        mensagem = {
            'mensagem': 'Não é possível excluir funcionario, excluir o funcionario selecionado exigiria excluir as frequências registradas.'}
        return render(request,'utils/pagina_erro.html',mensagem)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def funcionario_detail(request,pk):
    try:
        funcionario = Funcionario.objects.get(id=pk)
        return render(request, 'Funcionario/exibirFuncionario.html', {'funcionario': funcionario})
    except Funcionario.DoesNotExist:
        mensagem = {
            'mensagem': 'O funcionario não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.add_funcionario',login_url='erro_permissao')
def funcionario_new(request):
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST)
        if(form.is_valid()):
            funcionario = form.save()
            if request.FILES.get('foto'): funcionario.foto = request.FILES['foto']
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            funcionario.set_password(request.POST['senha'])
            grupoFuncionario = Group.objects.get(name='Funcionarios')
            grupoFuncionario.user_set.add(funcionario)
            funcionario.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
        dados={'form':form}
        return render(request,'Funcionario/funcionario_form.html',dados)

@permission_required('appPonto.change_funcionario',login_url='erro_permissao')
def funcionario_update(request, pk):
    try:
        funcionario = Funcionario.objects.get(id=pk)
    except Exception:
        mensagem = {
            'mensagem': 'O funcionario não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if request.FILES.get('foto'):
        funcionario.foto = request.FILES['foto']
    if request.method =="POST":
        form =FuncionarioForm(request.POST,instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            if request.POST.get('senha'): funcionario.set_password(request.POST['senha'])
            funcionario.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {'form': form, 'funcionario': funcionario}
        return render(request, 'Funcionario/funcionario_form.html', dados)

@permission_required('appPonto.view_funcionario', login_url='erro_permissao')
def funcionarios(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(nome__icontains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio = ""
    paginator = Paginator(funcionarios, 8)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados = {'funcionarios': funcionarios, 'criterio': criterio, 'paginator': paginator, 'page_obj': funcionarios}
    return render(request, 'Frequencia/funcionarios.html', dados)

@permission_required('appPonto.view_funcionario', login_url='erro_permissao')
def administrador_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        administradores = Funcionario.objects.filter(cargo__nome_funcao='Administrador',
                                                     nome__icontains=criterio).order_by('nome')
    else:
        administradores = Funcionario.objects.filter(cargo__nome_funcao='Administrador').order_by('nome')
        criterio = ""
    paginator = Paginator(administradores, 10)
    page = request.GET.get('page')
    try:
        administradores = paginator.page(page)
    except PageNotAnInteger:
        administradores = paginator.page(1)
    except EmptyPage:
        administradores = paginator.page(paginator.num_pages)
    dados = {'administradores': administradores, 'criterio': criterio, 'paginator': paginator,
             'page_obj': administradores}
    return render(request, 'Administrador/administrador_list.html', dados)

@permission_required('appPonto.view_funcionario', login_url='erro_permissao')
def administrador_new(request):
    criterio = request.GET.get('criterio')
    if criterio:
        funcionarios = Funcionario.objects.filter(~Q(cargo__nome_funcao__contains='Administrador'),
                                                  nome__icontains=criterio).order_by('nome')
    else:
        funcionarios = Funcionario.objects.filter(~Q(cargo__nome_funcao__contains='Administrador'))
        criterio = ""
    paginator = Paginator(funcionarios, 7)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados = {'funcionarios': funcionarios, 'criterio': criterio, 'paginator': paginator, 'page_obj': funcionarios}
    return render(request, 'Administrador/administrador_form.html', dados)


@permission_required('appPonto.change_funcionario', login_url='erro_permissao')
def administrador_update(request, pk):
    try:
        funcionario = Funcionario.objects.get(id=pk)
    except Exception:
        mensagem = {
            'mensagem': 'O funcionario não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if request.FILES.get('foto'):
        funcionario.foto = request.FILES['foto']
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.username = funcionario.matricula
            funcionario.first_name = funcionario.nome
            if request.POST.get('senha'): funcionario.set_password(request.POST['senha'])
            funcionario.save()
            return redirect('administrador_list')
    else:
        form = FuncionarioForm(instance=funcionario)
        dados = {'form': form, 'funcionario': funcionario}
        return render(request, 'Administrador/administrador_edit.html', dados)

@permission_required('appPonto.view_funcionario', login_url='erro_permissao')
def adicionar_administrador(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    grupoAdministrador = Group.objects.get(name='Administradores')
    grupoFuncionario = Group.objects.get(name='Funcionarios')
    grupoFuncionario.user_set.remove(funcionario)
    grupoAdministrador.user_set.add(funcionario)
    funcionario.setCargo('Administrador')
    funcionario.save()
    return redirect('administrador_new')

@permission_required('appPonto.view_funcionario', login_url='erro_permissao')
def remover_administrador(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    grupoAdministrador = Group.objects.get(name='Administradores')
    grupoFuncionario = Group.objects.get(name='Funcionarios')
    grupoAdministrador.user_set.remove(funcionario)
    grupoFuncionario.user_set.add(funcionario)
    funcionario.setCargo('Professor')
    funcionario.save()
    return redirect('administrador_list')

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
    try:
        departamento = Departamento.objects.get(id=pk)
        if criterio:
            cargos = Cargo.objects.filter(departamento=departamento, nome_funcao__icontains=criterio).order_by(
                'nome_funcao')
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
        dados = {'cargos': cargos, 'criterio': criterio, 'paginator': paginator, 'page_obj': cargos,
                 'departamento': departamento}
        return render(request, 'Departamento/exibirDepartamento.html', dados)
    except Departamento.DoesNotExist:
        mensagem = {
            'mensagem': 'O Departamento não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

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
    try:
        departamento = Departamento.objects.get(id=pk)
    except Departamento.DoesNotExist:
        mensagem = {
            'mensagem': 'O Departamento não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
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
        mensagem = {
            'mensagem': 'Não é possível excluir departamento, o departamento selecionado está relacionado a um cargo.'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.view_cargo',login_url='erro_permissao')
def cargo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        cargos = Cargo.objects.filter(nome_funcao__icontains=criterio).order_by('nome_funcao')
    else:
        cargos = Cargo.objects.all().order_by('nome_funcao')
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
    try:
        cargo = Cargo.objects.get(id=pk)
    except Exception:
        mensagem = {'mensagem': 'Cargo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
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
    try:
        cargo = Cargo.objects.get(id=pk)
    except Exception:
        mensagem = {'mensagem': 'Cargo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
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
    try:
        cargo = Cargo.objects.get(id=pk)
        cargo.delete()
        return redirect('cargo_list')
    except Exception:
        mensagem = {
            'mensagem': 'Não é possível excluir cargo, o cargo selecionado está relacionado a um funcionário.'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.view_diasSemExpediente',login_url='erro_permissao')
def diasSemExpediente_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        diasSemExpediente = DiasSemExpediente.objects.filter(descricao__icontains=criterio).order_by('data')
    else:
        diasSemExpediente = DiasSemExpediente.objects.all().order_by('data')
        criterio =""
    paginator =Paginator(diasSemExpediente,10)
    page = request.GET.get('page')
    try:
        diasSemExpediente = paginator.page(page)
    except PageNotAnInteger:
        diasSemExpediente=paginator.page(1)
    except EmptyPage:
        diasSemExpediente = paginator.page(paginator.num_pages)
    dados={'diasSemExpedientes':diasSemExpediente,'criterio':criterio,'paginator':paginator,'page_obj':diasSemExpediente}
    return render(request, 'DiasSemExpediente/diasSemExpediente_list.html', dados)

@permission_required('appPonto.view_diasSemExpediente',login_url='erro_permissao')
def diasSemExpediente_new(request):
    if (request.method == 'POST'):
        form = DiasSemExpedienteForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('diasSemExpediente_list')
    else:
        form=DiasSemExpedienteForm()
        dados={'form':form}
        return render(request, 'DiasSemExpediente/diasSemExpediente_form.html', dados)

@permission_required('appPonto.view_diasSemExpediente',login_url='erro_permissao')
def diasSemExpediente_update(request,pk):
    try:
        diasSemExpediente = DiasSemExpediente.objects.get(id=pk)
    except Exception:
        mensagem = {'mensagem': 'Dia sem expediente não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if(request.method=='POST'):
        form=DiasSemExpedienteForm(request.POST,instance=diasSemExpediente)
        if (form.is_valid()):
            form.save()
            return redirect('diasSemExpediente_list')
    else:
        form = DiasSemExpedienteForm(instance=diasSemExpediente)
        dados = {'form': form,'diasSemExpediente':diasSemExpediente}
        return render(request, 'DiasSemExpediente/diasSemExpediente_form.html', dados)

@permission_required('appPonto.view_diasSemExpediente', login_url='erro_permissao')
def diasSemExpediente_delete(request,pk):
    try:
        diasSemExpediente = DiasSemExpediente.objects.get(id=pk)
        diasSemExpediente.delete()
        return redirect('diasSemExpediente_list')
    except Exception:
        mensagem = {
            'mensagem': 'Não é possível excluir dia sem expediente.'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.add_horario', login_url='erro_permissao')
def horario_new(request):
    if (request.method == 'POST') and request.POST.get('dias'):
        form = HorarioForm(request.POST)
        if form.is_valid():
            cargahoraria = request.POST['cargahoraria']
            id_pessoa = request.POST['pessoa']
            pessoa = Pessoa.objects.get(id=id_pessoa)
            dias = request.POST.getlist('dias')
            horario = Horario.objects.create(cargahoraria=cargahoraria, pessoa=pessoa, dias=dias)
            horario.save()
            return redirect('horario_list')
    else:
        form = HorarioForm()
        dados = {'form': form}
        return render(request, 'Horario/horario_form.html', dados)

@permission_required('appPonto.view_horario', login_url='erro_permissao')
def horario_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        horarios = Horario.objects.filter(pessoa__nome__icontains=criterio).order_by('dias')
    else:
        horarios = Horario.objects.all().order_by('dias')
        criterio = ""
    paginator = Paginator(horarios, 10)
    page = request.GET.get('page')
    try:
        horarios = paginator.page(page)
    except PageNotAnInteger:
        horarios = paginator.page(1)
    except EmptyPage:
        horarios = paginator.page(paginator.num_pages)
    dados = {'horarios': horarios, 'criterio': criterio, 'paginator': paginator, 'page_obj': horarios}
    return render(request, 'Horario/horario_list.html', dados)

@permission_required('appPonto.change_horario',login_url='erro_permissao')
def horario_update(request,pk):
    try:
        horario = Horario.objects.get(id=pk)
    except Exception:
        mensagem = {'mensagem': 'Horário não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if(request.method=='POST'):
        form=HorarioForm(request.POST,instance=horario)
        if (form.is_valid()):
            form.save()
            return redirect('horario_list')
    else:
        form = HorarioForm(instance=horario)
        dados = {'form': form,'horario':horario}
        return render(request, 'Horario/horario_form.html', dados)

@permission_required('appPonto.delete_horario',login_url='erro_permissao')
def horario_delete(request,pk):
    try:
        horario = Horario.objects.get(id=pk)
        horario.delete()
        return redirect('horario_list')
    except Exception:
        mensagem = {
            'mensagem': 'Não é possível excluir Hórario.'}
        return render(request,'utils/pagina_erro.html',mensagem)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def horario_detail(request,pk):
    try:
        horario = Horario.objects.get(id=pk)
        return render(request, 'Horario/exibirhorario.html', {'horario': horario})
    except Horario.DoesNotExist:
        mensagem = {
            'mensagem': 'O Horário não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def funcionario_frequencia(request):
    if request.method == 'POST':
        if "frequencia_id" in request.POST:
            id_frequencia = int(request.POST['frequencia_id'])
            frequencia = Frequencia.objects.get(pk=id_frequencia)
            frequencia.observacao = request.POST['observacao']
            if request.FILES.get('arquivo'):frequencia.arquivo = request.FILES['arquivo']
            frequencia.save()
    id_funcionario = request.user.id
    try:
        funcionario = Funcionario.objects.get(id=id_funcionario)
    except Funcionario.DoesNotExist:
        return render(request, 'utils/permissao.html')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if Frequencia.validarData(data_inicial) and Frequencia.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = Frequencia.frequencias(data_inicial_formatada, data_final_formatada, funcionario)
        quantidade_presencas = Frequencia.quantidadePresenca(frequencias)
        quantidade_faltas = Frequencia.quantidadeFaltas(frequencias)
        horas_total = Frequencia.tempoTotal(frequencias)
        dados = {'frequencias': frequencias, 'funcionario': funcionario, 'data_inicial': data_inicial,
                 'data_final': data_final, 'quantidade_presenca': quantidade_presencas,
                 'quantidade_faltas': quantidade_faltas, 'horas_total': horas_total}
        return render(request, 'Frequencia/exibir_frequencia_funcionario.html', dados)
    else:
        dados = {'data': 'Data inválida'}
        return render(request, 'Frequencia/busca_frequencia.html', dados)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def funcionario_frequencias(request,pk):
    if request.method == 'POST':
        if "id_frequencia" in request.POST:
            id_frequencia = int(request.POST['id_frequencia'])
            frequencia = Frequencia.objects.get(pk=id_frequencia)
            frequencia.inconsistencia = False
            frequencia.save()
        if request.method == 'POST':
            if "frequencia_id" in request.POST:
                id_frequencia = int(request.POST['frequencia_id'])
                frequencia = Frequencia.objects.get(pk=id_frequencia)
                frequencia.observacao = request.POST['observacao']
                if request.FILES.get('arquivo'): frequencia.arquivo = request.FILES['arquivo']
                frequencia.save()
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    try:
        funcionario = Funcionario.objects.get(id=pk)
    except Funcionario.DoesNotExist:
        mensagem = {
            'mensagem': 'Funcionario não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

    if Frequencia.validarData(data_inicial) and Frequencia.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = Frequencia.frequencias(data_inicial_formatada, data_final_formatada, funcionario)
        quantidade_presencas = Frequencia.quantidadePresenca(frequencias)
        quantidade_faltas = Frequencia.quantidadeFaltas(frequencias)
        horas_total = Frequencia.tempoTotal(frequencias)
        dados = {'frequencias': frequencias, 'funcionario': funcionario, 'data_inicial': data_inicial,
                 'data_final': data_final, 'quantidade_presenca': quantidade_presencas,
                 'quantidade_faltas': quantidade_faltas, 'horas_total': horas_total}
        return render(request, 'Frequencia/exibir_frequencia_funcionario_admin.html', dados)
    else:
        dados = {'data': 'Data inválida', 'funcionario': funcionario}
        return render(request, 'Frequencia/busca_frequencia.html', dados)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def busca_frequencia(request):
    try:
        id_pessoa = request.user.id
        pessoa = Pessoa.objects.get(id=id_pessoa)
        return render(request, 'Frequencia/busca_frequencia.html')
    except Pessoa.DoesNotExist:
        return render(request, 'utils/permissao.html')

@permission_required('appPonto.view_frequencia', login_url='erro_permissao')
def busca_frequencia_funcionario(request, pk):
    try:
        funcionario = Funcionario.objects.get(id=pk)
        return render(request, 'Frequencia/busca_frequencia_funcionario.html', {'funcionario': funcionario})
    except Pessoa.DoesNotExist:
        mensagem = {
            'mensagem': 'O pessoa não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@login_required(login_url='login')
def perfil_funcionario(request):
    try:
        id_funcionario = request.user.id
        funcionario = Funcionario.objects.get(id=id_funcionario)
        return render(request, 'Perfil/perfil_funcionario.html', {'funcionario': funcionario})
    except Funcionario.DoesNotExist:
        return render(request, 'utils/permissao.html', )
