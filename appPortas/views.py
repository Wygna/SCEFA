from django.contrib.auth.decorators import permission_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from appPortas.forms import *
from appPortas.models import *


@permission_required('appPortas.view_porta', login_url='erro_permissao')
def porta_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        portas = Porta.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        portas = Porta.objects.all().order_by('descricao')
        criterio = ""
    paginator = Paginator(portas, 8)
    page = request.GET.get('page')
    try:
        portas = paginator.page(page)
    except PageNotAnInteger:
        portas = paginator.page(1)
    except EmptyPage:
        portas = paginator.page(paginator.num_pages)
    dados = {'portas': portas, 'criterio': criterio, 'paginator': paginator, 'page_obj': portas}
    return render(request, 'Portas/portas_list.html', dados)


@permission_required('appPortas.view_porta', login_url='erro_permissao')
def porta_detail(request, pk):
    criterio = request.GET.get('criterio')
    grupo = request.GET.get('grupo')
    porta = Porta.objects.get(id=pk)
    if grupo:
        porta_grupo = GrupoPorta.objects.get(porta=porta, grupo_id=grupo)
        porta_grupo.delete()
    if criterio:
        grupos = Grupo.objects.filter(grupoporta__porta=porta, descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.filter(grupoporta__porta=porta)
    criterio = ""
    paginator = Paginator(grupos, 10)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos = paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados = {'grupos': grupos, 'porta': porta, 'criterio': criterio, 'paginator': paginator, 'page_obj': grupos}
    return render(request, 'Portas/exibirPorta.html', dados)


@permission_required('appPortas.add_porta', login_url='erro_permissao')
def porta_new(request):
    if (request.method == 'POST'):
        form = PortaForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('porta_list')
    else:
        form = PortaForm()
        dados = {'form': form}
        return render(request, 'Portas/porta_form.html', dados)


@permission_required('appPortas.change_porta', login_url='erro_permissao')
def porta_update(request, pk):
    porta = Porta.objects.get(id=pk)
    if(request.method == 'POST'):
        form = PortaForm(request.POST, instance=porta)
        if (form.is_valid()):
            form.save()
            return redirect('porta_list')
    else:
        form = PortaForm(instance=porta)
        dados = {'form': form, 'porta': porta}
        return render(request, 'Portas/porta_form.html', dados)


@permission_required('appPortas.delete_porta', login_url='erro_permissao')
def porta_delete(request, pk):
    try:
        porta = Porta.objects.get(id=pk)
        porta.delete()
        return redirect('porta_list')
    except Exception:
        mensagem = {'mensagem': 'Não é possível excluir porta, a porta selecionado está relacionado a um grupo'}
        return render(request, 'utils/pagina_erro.html', mensagem)


@permission_required('appPortas.view_grupo', login_url='erro_permissao')
def grupo_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio = ""
    paginator = Paginator(grupos, 10)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos = paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados = {'grupos': grupos, 'criterio': criterio, 'paginator': paginator, 'page_obj': grupos}
    return render(request, 'Grupo/grupo_list.html', dados)


@permission_required('appPortas.view_grupo', login_url='erro_permissao')
def grupo_detail(request, pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    try:
        grupo = Grupo.objects.get(id=pk)
    except Grupo.DoesNotExist:
        mensagem = {
            'mensagem': 'Grupo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if usuario:
        try:
            usuario_grupo = GrupoPessoa.objects.get(pessoa_id=usuario, grupo=grupo)
            usuario_grupo.delete()
        except GrupoPessoa.DoesNotExist:
            mensagem = {
                'mensagem': 'Usuário não existe'}
            return render(request, 'utils/pagina_erro.html', mensagem)
    if criterio:
        usuarios_acesso = Pessoa.objects.filter(grupopessoa__grupo=grupo,
                                                nome__icontains=criterio).order_by('nome')
    else:
        usuarios_acesso = Pessoa.objects.filter(grupopessoa__grupo=grupo).order_by('nome')
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
    return render(request, 'Grupo/exibirGrupo.html', dados)


@permission_required('appPortas.add_grupo', login_url='erro_permissao')
def grupo_new(request):
    if (request.method == 'POST'):
        form = GrupoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('grupo_list')
    else:
        form = GrupoForm()
        dados = {'form': form}
        return render(request, 'Grupo/grupo_form.html', dados)


@permission_required('appPortas.change_grupo', login_url='erro_permissao')
def grupo_update(request, pk):
    try:
        grupo = Grupo.objects.get(id=pk)
    except Grupo.DoesNotExist:
        mensagem = {
            'mensagem': 'Grupo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if(request.method == 'POST'):
        form = PortaForm(request.POST, instance=grupo)
        if (form.is_valid()):
            form.save()
            return redirect('grupo_list')
    else:
        form = PortaForm(instance=grupo)
        dados = {'form': form, 'grupo': grupo}
        return render(request, 'Grupo/grupo_form.html', dados)


@permission_required('appPortas.delete_grupo', login_url='erro_permissao')
def grupo_delete(request, pk):
    try:
        grupo = Grupo.objects.get(id=pk)
        grupo.delete()
        return redirect('grupo_list')
    except Exception:
        mensagem = {
            'mensagem': 'Não é possível excluir grupo, o grupo tem portas relacionadas'}
        return render(request, 'utils/pagina_erro.html', mensagem)


@permission_required('appPonto.view_pessoa', login_url='erro_permissao')
def usuario_sem_acesso_grupo(request, pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    try:
        grupo = Grupo.objects.get(id=pk)
    except Grupo.DoesNotExist:
        mensagem = {
            'mensagem': 'Grupo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if usuario:
        try:
            usuario_grupo = GrupoPessoa(grupo=grupo, pessoa_id=usuario)
            usuario_grupo.save()
        except GrupoPessoa.DoesNotExist:
            mensagem = {
                'mensagem': 'Usuário não existe'}
            return render(request, 'utils/pagina_erro.html', mensagem)
    if criterio:
        usuarios_sem_acesso = Pessoa.objects.filter(~Q(grupopessoa__grupo=grupo),
                                                    nome__icontains=criterio).order_by('nome')
    else:
        usuarios_sem_acesso = Pessoa.objects.filter(~Q(grupopessoa__grupo=grupo)).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios_sem_acesso, 8)
    page = request.GET.get('page')
    try:
        usuarios_sem_acesso = paginator.page(page)
    except PageNotAnInteger:
        usuarios_sem_acesso = paginator.page(1)
    except EmptyPage:
        usuarios_sem_acesso = paginator.page(paginator.num_pages)
    dados = {'usuarios_sem_acesso': usuarios_sem_acesso, 'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios_sem_acesso}
    return render(request, 'Acesso/usuario_sem_acesso_grupo.html', dados)


@permission_required('appPonto.view_pessoa', login_url='erro_permissao')
def usuario_acesso_grupo(request, pk):
    criterio = request.GET.get('criterio')
    usuario = request.GET.get('usuario')
    try:
        grupo = Grupo.objects.get(id=pk)
    except Grupo.DoesNotExist:
        mensagem = {
            'mensagem': 'Grupo não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    if usuario:
        try:
            usuario_grupo = GrupoPessoa.objects.get(pessoa_id=usuario, grupo=grupo)
            usuario_grupo.delete()
        except GrupoPessoa.DoesNotExist:
            mensagem = {
                'mensagem': 'Usuário não existe'}
            return render(request, 'utils/pagina_erro.html', mensagem)
    if criterio:
        usuarios_acesso = Pessoa.objects.filter(grupopessoa__grupo=grupo,
                                                nome__icontains=criterio).order_by('nome')
    else:
        usuarios_acesso = Pessoa.objects.filter(grupopessoa__grupo=grupo).order_by('nome')
        criterio = ""
    paginator = Paginator(usuarios_acesso, 10)
    page = request.GET.get('page')
    try:
        usuarios_acesso = paginator.page(page)
    except PageNotAnInteger:
        usuarios_acesso = paginator.page(1)
    except EmptyPage:
        usuarios_acesso = paginator.page(paginator.num_pages)
    dados = {'usuarios_acesso': usuarios_acesso, 'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': usuarios_acesso}
    return render(request, 'Acesso/usuario_acesso_grupo.html', dados)


@permission_required('appPortas.view_porta', login_url='erro_permissao')
def porta_nao_grupo(request, pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        try:
            porta_grupo = GrupoPorta(grupo=grupo, porta_id=porta)
            porta_grupo.save()
        except GrupoPorta.DoesNotExist:
            mensagem = {
                'mensagem': 'Porta não existe'}
            return render(request, 'utils/pagina_erro.html', mensagem)
    if criterio:
        porta_nao_grupo = Porta.objects.filter(~Q(grupoporta__grupo=grupo),
                                               descricao__icontains=criterio).order_by('descricao')
    else:
        porta_nao_grupo = Porta.objects.filter(~Q(grupoporta__grupo=grupo)).order_by('descricao')
        criterio = ""
    paginator = Paginator(porta_nao_grupo, 8)
    page = request.GET.get('page')
    try:
        porta_nao_grupo = paginator.page(page)
    except PageNotAnInteger:
        porta_nao_grupo = paginator.page(1)
    except EmptyPage:
        porta_nao_grupo = paginator.page(paginator.num_pages)
    dados = {'porta_nao_grupo': porta_nao_grupo, 'grupo': grupo, 'criterio': criterio, 'paginator': paginator,
             'page_obj': porta_nao_grupo}
    return render(request, 'Acesso/porta_nao_grupo.html', dados)


@permission_required('appPortas.view_porta', login_url='erro_permissao')
def porta_no_grupo(request, pk):
    criterio = request.GET.get('criterio')
    porta = request.GET.get('porta')
    grupo = Grupo.objects.get(id=pk)
    if porta:
        try:
            porta_grupo = GrupoPorta.objects.get(porta=porta, grupo=grupo)
            porta_grupo.delete()
        except GrupoPorta.DoesNotExist:
            mensagem = {
                'mensagem': 'Porta não existe'}
            return render(request, 'utils/pagina_erro.html', mensagem)
    if criterio:
        porta_no_grupo = Porta.objects.filter(grupoporta__grupo=grupo,
                                              descricao__icontains=criterio).order_by('descricao')
    else:
        porta_no_grupo = Porta.objects.filter(grupoporta__grupo=grupo).order_by('descricao')
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


@permission_required('appPortas.view_grupo', login_url='erro_permissao')
def edit_grupo(request):
    criterio = request.GET.get('criterio')
    if criterio:
        grupos = Grupo.objects.filter(descricao__icontains=criterio).order_by('descricao')
    else:
        grupos = Grupo.objects.all().order_by('descricao')
        criterio = ""
    paginator = Paginator(grupos, 8)
    page = request.GET.get('page')
    try:
        grupos = paginator.page(page)
    except PageNotAnInteger:
        grupos = paginator.page(1)
    except EmptyPage:
        grupos = paginator.page(paginator.num_pages)
    dados = {'grupos': grupos, 'criterio': criterio, 'paginator': paginator, 'page_obj':grupos}
    return render(request, 'Acesso/edit_grupo.html', dados)


@permission_required('appPonto.view_pessoa', login_url='erro_permissao')
def portas(request):
    criterio = request.GET.get('criterio')
    if criterio:
        portas = Porta.objects.filter(nome__icontains=criterio).order_by('descricao')
    else:
        portas = Porta.objects.all().order_by('descricao')
        criterio = ""
    paginator = Paginator(portas, 8)
    page = request.GET.get('page')
    try:
        portas = paginator.page(page)
    except PageNotAnInteger:
        portas = paginator.page(1)
    except EmptyPage:
        portas = paginator.page(paginator.num_pages)
    dados = {'portas': portas, 'criterio': criterio, 'paginator': paginator, 'page_obj': portas}
    return render(request, 'Registro_Porta/portas.html', dados)


@permission_required('appPortas.view_registro_porta', login_url='erro_permissao')
def busca_porta_frequencia(request):
    try:
        id_pessoa = request.user.id
        pessoa = Pessoa.objects.get(id=id_pessoa)
        return render(request, 'Registro_Porta/busca_frequencia_porta.html')
    except Pessoa.DoesNotExist:
        return render(request, 'utils/permissao.html')


@permission_required('appPortas.view_registro_porta', login_url='erro_permissao')
def busca_porta(request, pk):
    try:
        porta = Porta.objects.get(id=pk)
        return render(request, 'Registro_Porta/busca_frequencia_porta.html', {'porta': porta})
    except Porta.DoesNotExist:
        return render(request, 'utils/permissao.html')


@permission_required('appPortas.view_registro_porta', login_url='erro_permissao')
def porta_frequencias(request, pk):
    try:
        porta = Porta.objects.get(id=pk)
    except Exception:
        mensagem = {
            'mensagem': 'Porta não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if RegistroPorta.validarData(data_inicial) and RegistroPorta.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = porta.registroporta_set.filter(data__gte=data_inicial_formatada,
                                                     data__lte=data_final_formatada).order_by('data')
        dados = {'frequencias': frequencias, 'porta': porta, 'data_inicial': data_inicial,
                 'data_final': data_final}
        return render(request, 'Registro_Porta/exibir_frequencia_porta.html', dados)
    else:
        return render(request, 'utils/permissao.html')


@permission_required('appPortas.view_registro_porta', login_url='erro_permissao')
def frequencia_porta_acesso(request):
    id_pessoa = request.user.id
    try:
        pessoa = Pessoa.objects.get(id=id_pessoa)
    except Exception:
        mensagem = {
            'mensagem': 'Usuário não existe'}
        return render(request, 'utils/pagina_erro.html', mensagem)
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if RegistroPorta.validarData(data_inicial) and RegistroPorta.validarData(data_final):
        data_inicial_formatada = datetime.datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
        data_final_formatada = datetime.datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")
        frequencias = pessoa.registroporta_set.filter(data__gte=data_inicial_formatada,
                                                      data__lte=data_final_formatada).order_by('data')
        dados = {'frequencias': frequencias, 'pessoa': pessoa, 'data_inicial': data_inicial,
                 'data_final': data_final}
        return render(request, 'Registro_Porta/exibir_frequencia_porta_pessoa.html', dados)
    else:
        dados = {'data': 'Data inválida'}
        return render(request, 'Registro_Porta/busca_frequencia_porta.html', dados)
