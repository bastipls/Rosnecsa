from django.shortcuts import render,redirect,get_object_or_404,redirect#Y29waW9u 
from .models import Tecnico,Empresa_tecnico,Cliente
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from rosnecsa.forms import FolioForm,TecnicoForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('txtuser',True)
        password = request.POST['txtpass']#Y29waW9u
        user = authenticate(request,username=username ,password = password)
        if user: 
            login(request,user)
            return HttpResponseRedirect(reverse('listar_clientes'))
         
        else:
            context["error"] = "Credenciales Incorrectas"
            return render(request, 'rosnecsa/login.html',context)    
    return render(request , 'rosnecsa/login.html',context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)#Y29waW9u
    return redirect('login')
    
def registro_inicial(request):#Y29waW9u
    
  
    context = {}
    if not request.user.is_anonymous:
        return redirect('login')
    else:
        
       
        if request.method == 'POST':
                rutTecnico = request.POST['txtrut']
                nombreTecnico = request.POST['txtname']
                apellidoTecnico = request.POST['txtlastname']
                emailTecnico = request.POST['txtemail']#Y29waW9u   
                contraseñaTecnico = request.POST['txtpass']

                empleado = Empresa_tecnico.objects.all()

                existe = False
                for i in empleado:

                    if emailTecnico == i.email_empleado:
                        existe = True

                if existe == True:  

                    user = User.objects.create_user(username=emailTecnico,email=emailTecnico,password=contraseñaTecnico,first_name=nombreTecnico,last_name=apellidoTecnico,is_staff=True)#Y29waW9u 
                    user.save()       
                    atributos =  Tecnico(rut_tecnico = rutTecnico,#Y29waW9u 
                                        email_tecnico = emailTecnico,
                                        nombre_tecnico = nombreTecnico,
                                        apellido_tecnico = apellidoTecnico)
                  
                    atributos.save()
                    # context["success"] = "Cuenta creada con exito"
                    # return render(request,'rosnecsa/login.html',context)
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return redirect('error')

        return render(request,'rosnecsa/registro_inicial.html',context)
def error (request):
    context ={}

    return render(request,'rosnecsa/error.html')
def listar_clientes (request):
    if  not request.user.is_superuser:

        tecnico = Tecnico.objects.get(email_tecnico = request.user.email)

        clientes_tecnico = Tecnico.objects.filter(rut_tecnico=tecnico).values("cliente__nombre_cliente")
        clientes = Cliente.objects.filter(nombre_cliente__in=clientes_tecnico)
       
        context = {'clientes':clientes}
        return render(request,'rosnecsa/listar_clientes.html',context)

    elif request.user.is_superuser:

        todos_clientes = Cliente.objects.all()
        context = {'todos_clientes':todos_clientes}


        return render(request,'rosnecsa/listar_clientes.html',context)

def crear_folio(request):
    if request.method == 'POST':
        form = FolioForm(request.POST)
        if form.is_valid():
            folion = form.save(commit=False)
            folion.save()
            return redirect('listar_clientes')
    else:
        form = FolioForm()           
    context={'form':form}
    return render(request,'rosnecsa/crear_folio.html',context)

def listar_tecnicos(request):
    tec = Tecnico.objects.all()
    context = {'tec':tec}

    return render(request,'rosnecsa/listar_tecnicos.html',context)
def asignar_cliente (request,pk):
    tecnico = get_object_or_404(Tecnico,pk=pk)
    if request.method == 'POST':
        form = TecnicoForm(request.POST,instance=tecnico)
        if form.is_valid():
            tecnico = form.save(commit=False)
            form.save_m2m()
            return redirect('listar_tecnicos')
    else:
        form = TecnicoForm(instance=tecnico)
    context= {'form':form}
    return render(request,'rosnecsa/asignar_cliente.html',context)            
