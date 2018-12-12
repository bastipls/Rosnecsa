from django.shortcuts import render,redirect,get_object_or_404
from .models import Tecnico
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('txtuser',True)
        password = request.POST['txtpass']
        user = authenticate(request,username=username ,password = password)
        if user: 
            login(request,user)
            return HttpResponseRedirect(reverse('crear_folio'))
        else:
            context["error"] = "Credenciales Incorrectas"
            return render(request, 'rosnecsa/login.html',context)    
    return render(request , 'rosnecsa/login.html',context)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
    
def registro_inicial(request):

    context = {}

    return render(request,'rosnecsa/registro_inicial.html',context)

def crear_folio(request):

    context={}

    return render(request,'rosnecsa/crear_folio.html')