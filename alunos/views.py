from django.conf.locale import id
from django.shortcuts import render, redirect
from django.db.models.fields import Empty


from alunos.froms import AlunoForm


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
