from django.forms import ModelForm,forms
from django import forms

from appPortas.models import *

class PortaForm(ModelForm):
    class Meta:
        model = Porta
        fields = ('descricao',)