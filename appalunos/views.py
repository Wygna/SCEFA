from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from appAlunos.forms import AlunoForm
from appAlunos.models import *
from appPonto.funcoes import *


@permission_required('appAlunos.add_aluno', login_url='erro_permissao')
def aluno_new(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.foto = request.FILES['foto']
            aluno.username = aluno.matricula
            aluno.first_name = aluno.nome
            aluno.set_password(aluno.senha)
            grupoAluno = Group.objects.get(name='Alunos')
            grupoAluno.user_set.add(aluno)
            aluno.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm
        dados = {'form': form}
        return render(request, 'Alunos/aluno_form.html', dados)


@permission_required('appAlunos.view_aluno', login_url='erro_permissao')
def aluno_detail(request, pk):
    aluno = Aluno.objects.get(id=pk)
    return render(request, 'Alunos/exibirAlunos.html',{'aluno':aluno})


@permission_required('appAlunos.view_aluno', login_url='erro_permissao')
def aluno_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        alunos = Aluno.objects.filter(nome__icontains=criterio).order_by('nome')
    else:
        alunos = Aluno.objects.all().order_by('nome')
        criterio = ''
    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos = paginator.page(1)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)
    dados = {'alunos': alunos, 'criterio': criterio,
             'paginator': paginator, 'page_obj': alunos}
    return render(request, 'Alunos/alunos_list.html', dados)


@permission_required('appAlunos.delete_aluno', login_url='erro_permissao')
def aluno_delete(request, pk):
    try:
        aluno = Aluno.objects.get(id=pk)
        aluno.delete()
        return redirect('aluno_list')
    except Exception:
        mensagem ={'mensagem':'Não é possível excluir aluno, excluir o aluno selecionado exigiria excluir as frequências registradas'}
        return render(request,'utils/pagina_erro.html',mensagem)


@permission_required('appAlunos.change_aluno', login_url='erro_permissao')
def aluno_update(request,pk):
    aluno = Aluno.objects.get(id=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.foto = request.FILES['foto']
            aluno.username = aluno.matricula
            aluno.first_name = aluno.nome
            aluno.set_password(aluno.senha)
            grupoAluno = Group.objects.get(name='Alunos')
            grupoAluno.user_set.add(aluno)
            aluno.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
        dados = {'form': form, 'aluno': aluno}
        return render(request, 'Alunos/aluno_form.html', dados)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def aluno_frequencia(request,pk):
    current_user = request.user
    try:
        aluno = Aluno.objects.get(id=pk)
        if aluno.matricula ==  current_user.username:
            data_inicial = request.GET.get('data_inicial')
            data_final = request.GET.get('data_final')
            if validar_data(data_inicial) and validar_data(data_final):
                data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
                data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
                frequencias = aluno.frequencia_set.filter(~Q(data__week_day=7),~Q(data__week_day=1),data__gte=data_inicial_formatada,data__lte=data_final_formatada).order_by('data')
                frequencia_com_expediente = []
                for frequencia in frequencias:
                    if frequencia.data not in datas_sem_expediente():
                        frequencia_com_expediente.append(frequencia)
                dias_trabalhados = dias_registrados(frequencia_com_expediente)
                dias_nao_trabalhados = dias_nao_registrados(frequencia_com_expediente)
                horas_total = tempo_total(frequencia_com_expediente)
                dados = {'frequencias':frequencia_com_expediente,'aluno':aluno,'data_inicial':data_inicial,
                         'data_final':data_final,'dias_trabalhos':dias_trabalhados,'dias_nao_trabalhos':dias_nao_trabalhados,'horas_total':horas_total}
                return render(request, 'Frequencia/exibir_frequencia_aluno.html', dados)
        else:
            return render(request,'utils/permissao.html')
    except Exception:
        mensagem = {
            'mensagem': 'Aluno não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def aluno_frequencias(request,pk):
    try:
        aluno = Aluno.objects.get(id=pk)
    except Exception:
        mensagem = {
            'mensagem': 'Aluno não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if validar_data(data_inicial) and validar_data(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = aluno.frequencia_set.filter(~Q(data__week_day=7), ~Q(data__week_day=1),
                                                  data__gte=data_inicial_formatada,
                                                  data__lte=data_final_formatada).order_by('data')
        frequencia_com_expediente = []
        for frequencia in frequencias:
            if frequencia.data not in datas_sem_expediente():
                frequencia_com_expediente.append(frequencia)
        dias_aulas = dias_registrados(frequencia_com_expediente)
        dias_nao_aulas = dias_nao_registrados(frequencia_com_expediente)
        horas_total = tempo_total(frequencia_com_expediente)
        dados = {'frequencias': frequencia_com_expediente, 'aluno': aluno, 'data_inicial': data_inicial,
                 'data_final': data_final, 'dias_aulas': dias_aulas, 'dias_nao_aulas': dias_nao_aulas,
                 'horas_total': horas_total}
        return render(request, 'Frequencia/exibir_frequencia_aluno.html', dados)
    else:
        return render(request, 'utils/permissao.html')

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def busca_aluno_frequencia(request, pk):
    aluno = Aluno.objects.get(id=pk)
    return render(request, 'Frequencia/busca_frequencia_aluno.html', {'aluno':aluno})

@permission_required('appAlunos.view_aluno', login_url='erro_permissao')
def alunos_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        alunos = Aluno.objects.filter(nome__icontains=criterio).order_by('nome')
    else:
        alunos = Aluno.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(alunos,10)
    page = request.GET.get('page')
    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos=paginator.page(1)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)
    dados={'alunos':alunos,'criterio':criterio,'paginator':paginator,'page_obj':alunos}
    return render(request, 'Frequencia/frequencia_aluno_list.html', dados)
