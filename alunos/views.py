from django.shortcuts import render, redirect
from django.db.models.fields import Empty

def home(request):
    return render('base.html')
