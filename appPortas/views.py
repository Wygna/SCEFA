from django.contrib.auth.decorators import permission_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from appPortas.forms import *
from appPortas.models import *


@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        portas = Porta.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        portas = Porta.objects.all().order_by('descricao')
        criterio =""
    paginator = Paginator(portas, 10)
    page = request.GET.get('page')
    try:
        portas = paginator.page(page)
    except PageNotAnInteger:
        portas=paginator.page(1)
    except EmptyPage:
        portas = paginator.page(paginator.num_pages)
    dados={'portas':portas,'criterio':criterio,'paginator':paginator,'page_obj':portas}
    return render(request, 'Portas/portas_list.html',dados)

@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_detail(request,pk):
    criterio = request.GET.get('criterio')
    grupo = request.GET.get('grupo')
    porta = Porta.objects.get(id=pk)
    if grupo:
        porta_grupo = Porta_Grupo.objects.get(porta=porta,grupo_id=grupo)
        porta_grupo.delete()
    if criterio:
        grupos = Grupo.objects.filter(porta_grupo__porta=porta,descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.filter(porta_grupo__porta=porta)
    criterio = ""
    paginator = Paginator(grupos, 10)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos = paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados = {'grupos': grupos,'porta':porta, 'criterio': criterio, 'paginator': paginator, 'page_obj': grupos}
    return render(request, 'Portas/exibirPorta.html', dados)

@permission_required('appPortas.add_porta',login_url='erro_permissao')
def porta_new(request):
    if (request.method == 'POST'):
        form = PortaForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('porta_list')
    else:
        form=PortaForm()
        dados={'form':form}
        return render(request,'Portas/porta_form.html',dados)

@permission_required('appPortas.change_porta',login_url='erro_permissao')
def porta_update(request,pk):
    porta = Porta.objects.get(id=pk)
    if(request.method=='POST'):
        form=PortaForm(request.POST,instance=porta)
        if (form.is_valid()):
            form.save()
            return redirect('porta_list')
    else:
        form = PortaForm(instance=porta)
        dados = {'form': form,'porta':porta}
        return render(request, 'Portas/porta_form.html', dados)

@permission_required('appPortas.delete_porta',login_url='erro_permissao')
def porta_delete(request,pk):
    try:
        porta =Porta.objects.get(id=pk)
        porta.delete()
        return redirect('porta_list')
    except Exception:
        mensagem ={'mensagem':'Não é possível excluir porta, a porta selecionado está relacionado a um grupo'}
        return render(request,'utils/pagina_erro.html',mensagem)

@permission_required('appPortas.view_grupo',login_url='erro_permissao')
def grupo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(grupos,10)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos=paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados={'grupos':grupos,'criterio':criterio,'paginator':paginator,'page_obj':grupos}
    return render(request, 'Grupo/grupo_list.html',dados)

@permission_required('appPortas.view_grupo',login_url='erro_permissao')
def grupo_detail(request,pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    grupo = Grupo.objects.get(id=pk)
    if usuario:
        usuario_grupo = Pessoa_Grupo.objects.get(pessoa_id=usuario,grupo=grupo)
        usuario_grupo.delete()
    if criterio:
        usuarios_acesso = Pessoa.objects.filter(pessoa_grupo__grupo=grupo,
                                                 nome__icontains=criterio).order_by('nome')
    else:
        usuarios_acesso = Pessoa.objects.filter(pessoa_grupo__grupo=grupo).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios_acesso, 5)
    page = request.GET.get('page')
    try:
        usuarios_acesso = paginator.page(page)
    except PageNotAnInteger:
        usuarios_acesso = paginator.page(1)
    except EmptyPage:
        usuarios_acesso = paginator.page(paginator.num_pages)
    dados = {'usuarios_acesso': usuarios_acesso, 'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios_acesso}
    return render(request,'Grupo/exibirGrupo.html',dados)

@permission_required('appPortas.add_grupo',login_url='erro_permissao')
def grupo_new(request):
    if (request.method == 'POST'):
        form = GrupoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('grupo_list')
    else:
        form=GrupoForm()
        dados={'form':form}
        return render(request,'Grupo/grupo_form.html',dados)

@permission_required('appPortas.change_grupo',login_url='erro_permissao')
def grupo_update(request,pk):
    grupo = Grupo.objects.get(id=pk)
    if(request.method=='POST'):
        form=PortaForm(request.POST,instance=grupo)
        if (form.is_valid()):
            form.save()
            return redirect('grupo_list')
    else:
        form = PortaForm(instance=grupo)
        dados = {'form': form,'grupo':grupo}
        return render(request, 'Grupo/grupo_form.html', dados)

@permission_required('appPortas.delete_grupo',login_url='erro_permissao')
def grupo_delete(request,pk):
    try:
        grupo = Grupo.objects.get(id=pk)
        grupo.delete()
        return redirect('grupo_list')
    except Exception:
        mensagem = {
            'mensagem': 'Não é possível excluir grupo, o grupo tem portas relacionadas'}
        return render(request, 'utils/pagina_erro.html', mensagem)

@permission_required('appPonto.view_pessoa',login_url='erro_permissao')
def usuario_sem_acesso_grupo(request,pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    grupo = Grupo.objects.get(id=pk)
    if usuario:
        usuario_grupo = Pessoa_Grupo(grupo=grupo,pessoa_id=usuario)
        usuario_grupo.save()
    if criterio:
        usuarios_sem_acesso = Pessoa.objects.filter(~Q(pessoa_grupo__grupo=grupo),
                                                     nome__icontains=criterio).order_by('nome')
    else:
        usuarios_sem_acesso = Pessoa.objects.filter(~Q(pessoa_grupo__grupo=grupo)).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios_sem_acesso, 5)
    page = request.GET.get('page')
    try:
        usuarios_sem_acesso = paginator.page(page)
    except PageNotAnInteger:
        usuarios_sem_acesso = paginator.page(1)
    except EmptyPage:
        usuarios_sem_acesso = paginator.page(paginator.num_pages)
    dados = {'usuarios_sem_acesso': usuarios_sem_acesso,'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios_sem_acesso}
    return render(request, 'Acesso/usuario_sem_acesso_grupo.html', dados)

@permission_required('appPonto.view_pessoa',login_url='erro_permissao')
def usuario_acesso_grupo(request, pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    grupo = Grupo.objects.get(id=pk)
    if usuario:
        usuario_grupo = Pessoa_Grupo.objects.get(pessoa_id=usuario,grupo=grupo)
        usuario_grupo.delete()
    if criterio:
        usuarios_acesso = Pessoa.objects.filter(pessoa_grupo__grupo=grupo,
                                                     nome__icontains=criterio).order_by('nome')
    else:
        usuarios_acesso = Pessoa.objects.filter(pessoa_grupo__grupo=grupo).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios_acesso, 5)
    page = request.GET.get('page')
    try:
        usuarios_acesso = paginator.page(page)
    except PageNotAnInteger:
        usuarios_acesso = paginator.page(1)
    except EmptyPage:
        usuarios_acesso = paginator.page(paginator.num_pages)
    dados = {'usuarios_acesso': usuarios_acesso,'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios_acesso}
    return render(request, 'Acesso/usuario_acesso_grupo.html', dados)

@permission_required('appPonto.view_pessoa',login_url='erro_permissao')
def grupo_usuario_list(request, pk):
    criterio = request.GET.get('criterio')
    grupo = Grupo.objects.get(id=4)
    if criterio:
        usuarios = Pessoa.objects.filter(pessoa_grupo__grupo=grupo,
                                                     nome__icontains=criterio).order_by('nome')
    else:
        usuarios = Pessoa.objects.filter(pessoa_grupo__grupo=grupo).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios, 10)
    page = request.GET.get('page')
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)
    dados = {'usuarios_acesso': usuarios,'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios}
    return render(request, 'Grupo/exibirGrupo.html', dados)

@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_nao_grupo(request, pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        porta_grupo = Porta_Grupo(grupo=grupo,porta_id=porta)
        porta_grupo.save()
    if criterio:
        porta_nao_grupo = Porta.objects.filter(~Q(porta_grupo__grupo=grupo),
                                                     descricao__icontains=criterio).order_by('descricao')
    else:
        porta_nao_grupo = Porta.objects.filter(~Q(porta_grupo__grupo=grupo)).order_by('descricao')
        criterio = ""
    paginator = Paginator(porta_nao_grupo, 5)
    page = request.GET.get('page')
    try:
        porta_nao_grupo = paginator.page(page)
    except PageNotAnInteger:
        porta_nao_grupo = paginator.page(1)
    except EmptyPage:
        porta_nao_grupo = paginator.page(paginator.num_pages)
    dados = {'porta_nao_grupo': porta_nao_grupo,'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': porta_nao_grupo}
    return render(request, 'Acesso/porta_nao_grupo.html', dados)

@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_no_grupo(request, pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        porta_grupo = Porta_Grupo.objects.get(porta=porta,grupo=grupo)
        porta_grupo.delete()
    if criterio:
        porta_no_grupo = Porta.objects.filter(porta_grupo__grupo=grupo,
                                              descricao__contains=criterio).order_by('descricao')
    else:
        porta_no_grupo = Porta.objects.filter(porta_grupo__grupo=grupo).order_by('descricao')
        criterio = ""
    paginator = Paginator(porta_no_grupo, 5)
    page = request.GET.get('page')
    try:
        porta_no_grupo = paginator.page(page)
    except PageNotAnInteger:
        porta_no_grupo = paginator.page(1)
    except EmptyPage:
        porta_nao_grupo = paginator.page(paginator.num_pages)
    dados = {'porta_no_grupo': porta_no_grupo, 'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': porta_no_grupo}
    return render(request, 'Acesso/porta_no_grupo_list.html', dados)

@permission_required('appPortas.view_grupo',login_url='erro_permissao')
def edit_grupo(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(grupos,8)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos=paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados={'grupos':grupos,'criterio':criterio,'paginator':paginator,'page_obj':grupos}
    return render(request, 'Acesso/edit_grupo.html', dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def adicionar_acesso_funcionario(request,pk):
    funcionario = Funcionario.objects.get()
    return redirect('administrador_new')
