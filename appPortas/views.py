from django.contrib.auth.management import get_default_username
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory
import datetime as DT
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm
from appPortas.forms import *
from appPortas.models import *
from appalunos.models import Aluno
from django.db.models import Q

@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        portas = Porta.objects.filter(descricao_name=criterio).order_by('descricao')
    else:
        portas = Porta.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(portas,4)
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
    porta = Porta.objects.get(id=pk)
    grupos = Porta_Grupo.objects.filter(porta=porta)
    return render(request,'Portas/exibirPorta.html',{'porta':porta,'grupos':grupos})

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

@permission_required('appPonto.delete_porta',login_url='erro_permissao')
def porta_delete(request,pk):
    porta =Porta.objects.get(id=pk)
    porta.delete()
    return redirect('porta_list')

@permission_required('appPortas.view_grupo',login_url='erro_permissao')
def grupo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao_name=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(grupos,4)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        portas=paginator.page(1)
    except EmptyPage:
        portas = paginator.page(paginator.num_pages)
    dados={'grupos':grupos,'criterio':criterio,'paginator':paginator,'page_obj':grupos}
    return render(request, 'Grupo/grupo_list.html',dados)

@permission_required('appPortas.view_grupo',login_url='erro_permissao')
def grupo_detail(request,pk):
    grupo = Grupo.objects.get(id=pk)
    grupo_usuarios = Usuario_Grupo.objects.filter(grupo=grupo)
    return render(request,'Grupo/exibirGrupo.html',{'grupo':grupo,'grupo_usuarios':grupo_usuarios})

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
    grupo = Grupo.objects.get(id=pk)
    grupo.delete()
    return redirect('grupo_list')

@permission_required('appPortas.view_usuario',login_url='erro_permissao')
def usuario_sem_acesso_grupo(request,pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    grupo = Grupo.objects.get(id=pk)
    if usuario:
        usuario_grupo = Usuario_Grupo(grupo=grupo,usuario_id=usuario)
        usuario_grupo.save()
    if criterio:
        usuarios_sem_acesso = Usuario.objects.filter(~Q(usuario_grupo__grupo=grupo),
                                                     pessoa__nome__contains=criterio).order_by('pessoa__nome')
    else:
        usuarios_sem_acesso = Usuario.objects.filter(~Q(usuario_grupo__grupo=grupo)).order_by('pessoa__nome')
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

@permission_required('appPortas.view_usuario',login_url='erro_permissao')
def usuario_acesso_grupo_list(request,pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    grupo = Grupo.objects.get(id=pk)
    if usuario:
        usuario_grupo = Usuario_Grupo.objects.get(usuario=usuario)
        usuario_grupo.delete()
    if criterio:
        usuarios_acesso = Usuario.objects.filter(usuario_grupo__grupo=grupo,
                                                     pessoa__nome__contains=criterio).order_by('pessoa__nome')
    else:
        usuarios_acesso = Usuario.objects.filter(usuario_grupo__grupo=grupo).order_by('pessoa__nome')
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
    return render(request, 'Acesso/usuario_acesso_grupo_list.html', dados)

@permission_required('appPortas.view_porta',login_url='erro_permissao')
def porta_nao_grupo_list(request,pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        porta_grupo = Porta_Grupo(grupo=grupo,porta_id=porta)
        porta_grupo.save()
    if criterio:
        porta_nao_grupo = Porta.objects.filter(~Q(porta_grupo__grupo=grupo),
                                                     descricao__contains=criterio).order_by('descricao')
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
def porta_no_grupo_list(request,pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        porta_grupo = Porta_Grupo.objects.get(porta=porta)
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
def acesso_grupo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao_name=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio =""
    paginator =Paginator(grupos,4)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        portas=paginator.page(1)
    except EmptyPage:
        portas = paginator.page(paginator.num_pages)
    dados={'grupos':grupos,'criterio':criterio,'paginator':paginator,'page_obj':grupos}
    return render(request, 'Acesso/acesso_grupo_list.html',dados)

@permission_required('appPonto.view_funcionario',login_url='erro_permissao')
def adicionar_acesso_funcionario(request,pk):
    funcionario = Funcionario.objects.get()

    return redirect('administrador_new')