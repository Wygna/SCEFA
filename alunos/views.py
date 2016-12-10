from django.conf.locale import id
from django.shortcuts import render, redirect
from django.db.models.fields import Empty


from alunos.forms import AlunoForm
from alunos.models import Aluno


def aluno_new(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos_list')
    else:
        form = AlunoForm
        dados = {'form': form}
        return render(request, 'Alunos/aluno_form.html', dados)


def aluno_detail(request, pk):
    aluno = Aluno.objects.get(id=pk)
    return render(request, 'Alunos/exibirAlunos.html')


def aluno_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        alunos = Aluno.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        alunos = Funcionario.objects.all().order_by('nome')
        criterio = ''
    return render(request, 'Alunos/alunos_list.html', dados)
