from django.shortcuts import render,redirect,get_object_or_404
from .models import Tecnico
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_view(request):
    context = {}

    return render(request , 'rosnecsa/login.html',context)

def registro_inicial(request):

    context = {}

    return render(request,'rosnecsa/registro_inicial.html',context)

def crear_folio(request):

    context={}

    return render(request,'rosnecsa/crear_folio.html')