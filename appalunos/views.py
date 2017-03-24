from django.conf.locale import id
from django.shortcuts import render, redirect
from django.db.models.fields import Empty
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required


from appalunos.forms import AlunoForm
from appalunos.models import Aluno


def aluno_new(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
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


def aluno_detail(request, pk):
    aluno = Aluno.objects.get(id=pk)
    return render(request, 'Alunos/exibirAlunos.html',{'aluno':aluno})


def aluno_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        alunos = Aluno.objects.filter(nome__contains=criterio).order_by('nome')
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


def aluno_delete(request, pk):
    aluno = Aluno.objects.get(id=pk)
    aluno.delete()
    return redirect('aluno_list')

def aluno_update(request,pk):
    aluno = Aluno.objects.get(id=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save()
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

def aluno_relatorio(request,pk):
    aluno = Aluno.objects.get(id=pk)
    registroPonto = aluno.registrarponto_set.all()
    return render(request,'RegistroPonto/exibirRegistroPontoAluno.html',{'registroPontos':registroPonto})

@permission_required('appPonto.view_relatorioPonto',login_url='erro_permissao')
def registroPonto_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        alunos = Aluno.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        alunos = Aluno.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(alunos,4)
    page = request.GET.get('page')
    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos=paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados={'alunos':alunos,'criterio':criterio,'paginator':paginator,'page_obj':alunos}
    return render(request, 'RegistroPonto/RegistroPontoAluno_list.html',dados)
