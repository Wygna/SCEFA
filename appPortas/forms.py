from django.forms import ModelForm,forms
from django import forms

from appPortas.models import *
from django.forms.models import inlineformset_factory

class PortaForm(ModelForm):
    class Meta:
        model = Porta
        fields = ('descricao',)

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ('descricao',)
