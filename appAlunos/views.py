from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from appAlunos.forms import AlunoForm
from appAlunos.models import *
from appPonto.models import *

@permission_required('appAlunos.add_aluno', login_url='erro_permissao')
def aluno_new(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            if request.FILES.get('foto'): aluno.foto = request.FILES['foto']
            aluno.username = aluno.matricula
            aluno.first_name = aluno.nome
            if request.POST.get('senha'): aluno.set_password(request.POST['senha'])
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
    try:
        aluno = Aluno.objects.get(id=pk)
        return render(request, 'Alunos/exibirAluno.html', {'aluno': aluno})
    except Aluno:
        mensagem = {
            'mensagem': 'O Aluno não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

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
    try:
        aluno = Aluno.objects.get(id=pk)
    except Exception:
        mensagem = {
            'mensagem': 'O Aluno não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save(commit=False)
            if request.FILES.get('foto'): aluno.foto = request.FILES['foto']
            aluno.username = aluno.matricula
            aluno.first_name = aluno.nome
            if request.POST.get('senha'): aluno.set_password(request.POST['senha'])
            aluno.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
        dados = {'form': form, 'aluno': aluno}
        return render(request, 'Alunos/aluno_form.html', dados)

@permission_required('appPonto.view_frequencia',login_url='erro_permissao')
def aluno_frequencia(request):
    if request.method == 'POST':
        if "frequencia_id" in request.POST:
            id_frequencia = int(request.POST['frequencia_id'])
            frequencia = Frequencia.objects.get(pk=id_frequencia)
            frequencia.observacao = request.POST['observacao']
            if request.FILES.get('arquivo'): frequencia.arquivo = request.FILES['arquivo']
            frequencia.save()
    id_aluno = request.user.id
    try:
        aluno = Aluno.objects.get(id=id_aluno)
    except Aluno.DoesNotExist:
        return render(request, 'utils/permissao.html')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if Frequencia.validarData(data_inicial) and Frequencia.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = Frequencia.frequencias(data_inicial_formatada, data_final_formatada, aluno)
        dias_aulas = Frequencia.quantidadePresenca(frequencias)
        dias_nao_aulas = Frequencia.quantidadeFaltas(frequencias)
        horas_total = Frequencia.tempoTotal(frequencias)
        dados = {'frequencias': frequencias, 'aluno': aluno, 'data_inicial': data_inicial,
                 'data_final': data_final, 'dias_aulas': dias_aulas, 'dias_nao_aulas': dias_nao_aulas,
                 'horas_total': horas_total}
        return render(request, 'Frequencia/exibir_frequencia_aluno.html', dados)
    else:
        dados = {'data': 'Data inválida'}
        return render(request, 'Frequencia/busca_frequencia.html', dados)

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
    if Frequencia.validarData(data_inicial) and Frequencia.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = Frequencia.frequencias(data_inicial_formatada, data_final_formatada, aluno)
        dias_aulas = Frequencia.quantidadePresenca(frequencias)
        dias_nao_aulas = Frequencia.quantidadeFaltas(frequencias)
        horas_total = Frequencia.tempoTotal(frequencias)
        dados = {'frequencias': frequencias, 'aluno': aluno, 'data_inicial': data_inicial,
                 'data_final': data_final, 'dias_aulas': dias_aulas, 'dias_nao_aulas': dias_nao_aulas,
                 'horas_total': horas_total}
        dados = {'frequencias': frequencias, 'aluno': aluno, 'data_inicial': data_inicial,
                 'data_final': data_final, 'dias_aulas': dias_aulas, 'dias_nao_aulas': dias_nao_aulas,
                 'horas_total': horas_total}
        return render(request, 'Frequencia/exibir_frequencia_aluno.html', dados)
    else:
        return render(request, 'utils/permissao.html')

@permission_required('appAlunos.view_aluno', login_url='erro_permissao')
def alunos(request):
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
    return render(request, 'Frequencia/alunos.html', dados)

@permission_required('appPonto.view_frequencia', login_url='erro_permissao')
def busca_frequencia_aluno(request, pk):
    try:
        aluno = Aluno.objects.get(id=pk)
        return render(request, 'Frequencia/busca_frequencia_aluno.html', {'aluno': aluno})
    except Aluno.DoesNotExist:
        mensagem = {
            'mensagem': 'O Aluno não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@login_required(login_url='login')
def perfil_aluno(request):
    try:
        id_aluno = request.user.id
        aluno = Aluno.objects.get(id=id_aluno)
        return render(request, 'Perfil/perfil_aluno.html', {'aluno': aluno})
    except Aluno.DoesNotExist:
        return render(request, 'utils/permissao.html', )
