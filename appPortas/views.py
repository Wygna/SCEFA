from django.contrib.auth.management import get_default_username
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory
import datetime as DT
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm
from appPortas.forms import *
from appPortas.models import *


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
    return render(request,'Portas/exibirPorta.html',{'porta':porta})

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

@permission_required('appPortas.update_porta',login_url='erro_permissao')
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