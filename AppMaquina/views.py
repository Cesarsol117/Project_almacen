from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMaquina.forms import *
# clases
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# -------------
# para el formulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
# para restriciones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
# def herramienta(request):
#     herramienta = Herramienta(nombre="llave inglesa", cantidad = 6, ubicacion = "a4")
#     herramienta.save()
#     cadena_texto = "herramienta guardada: "+herramienta.nombre+" "+"La cantidad es: "+ str(herramienta.cantidad)+" "+"su ubicacion es: "+ herramienta.ubicacion
#     return HttpResponse(cadena_texto)


def inicio(request):
    return render(request, "AppMaquina/inicio.html")

# formularios
@login_required
def insumos(request):
    if request.method == 'POST':
        form=InsuFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            cantidad = informacion["cantidad"]
            ubicacion = informacion["ubicacion"]
            fecha_vence = informacion["fecha_vence"]

            insu = Insumos(nombre=nombre, cantidad=cantidad, ubicacion=ubicacion, fecha_vence=fecha_vence)
            insu.save()
            return render(request, "AppMaquina/inicio.html")
    else:
        formulario = InsuFormulario() 
        
    return render(request, "AppMaquina/insumos.html", {"form":formulario}) 
@login_required
def repuestos(request):
    if request.method =='POST':
        form = RepuFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre= informacion["nombre"]
            maquina= informacion["maquina"]
            cantidad= informacion["cantidad"]
            ubicacion= informacion["ubicacion"]

            repu= Repuestos(nombre=nombre, maquina=maquina, cantidad=cantidad, ubicacion=ubicacion)
            repu.save()
            return render(request,"AppMaquina/inicio.html")
    else:
        formulario = RepuFormulario()
    return render(request, "AppMaquina/repuestos.html", {"form":formulario})
@login_required
def tecnico(request):
    if request.method == 'POST':
        form = TecFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            email = informacion["email"]

            tecni = Tecnico(nombre=nombre, email=email)
            tecni.save()
            return render(request,"AppMaquina/inicio.html")
    else:
        formulario = TecFormulario()
    return render(request, "AppMaquina/tecnico.html", {"form":formulario})
@login_required
def herramienta(request):
    if request.method == 'POST':
        form=HerraFormulario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            cantidad = informacion["cantidad"]
            ubicacion = informacion["ubicacion"]

            herra = Herramienta(nombre=nombre, cantidad=cantidad, ubicacion=ubicacion)
            herra.save()
            return render(request, "AppMaquina/inicio.html")
        else:
            return render(request, "AppMaquina/herramienta.html", {"form":formulario}) 
    else:
        formulario = HerraFormulario() 

    return render(request, "AppMaquina/herramienta.html", {"form":formulario}) 
# busquedas

# pagina principal
@login_required
def busqueda(request):
    return render(request, "AppMaquina/busacar.html")
# pagina de busqueda herrramientas
@login_required
def busquedaherra(request):
    return render(request, "AppMaquina/busquedaherra.html")
# pagina de busqueda insumos
@login_required
def busquedainsumos(request):
    return render(request, "AppMaquina/busquedainsumos.html")
# pagina de busqueda Repuestos
@login_required
def busquedaRepuestos(request):
    return render(request, "AppMaquina/busquedaRepuestos.html")
@login_required
def buscar(request):
    if request.GET["cosa"]:
        search = request.GET["cosa"]
        herramienta1 = Herramienta.objects.filter(nombre__icontains=search)
        return render(request, "AppMaquina/resultadosbusqueda.html", {"herramientas":herramienta1})
    else:
        return render(request, "AppMaquina/busquedaherra.html", {"mensaje": "no lleno nada"})
# <------------------------------------Resultados Insumos -------------------------------------------------------------------->

@login_required
def buscarInsu(request):
    if request.GET["algo"]:
        search = request.GET["algo"]
        insumo1 = Insumos.objects.filter(nombre__icontains=search)
        return render(request, "AppMaquina/resultadosInsumos.html", {"insumos":insumo1})
    else:
        return render(request, "AppMaquina/busquedaInsumos.html", {"mensaje": "no lleno nada"})
# <---------------------------------------------------------------------------------------------------------------------------->
# <------------------------------------Resultados Repuestos -------------------------------------------------------------------->

@login_required
def buscarRepu(request):
    if request.GET["esto"]:
        search = request.GET["esto"]
        repuestos1 = Repuestos.objects.filter(nombre__icontains=search)
        return render(request, "AppMaquina/resultadoRepuestos.html", {"repue":repuestos1})
    else:
        return render(request, "AppMaquina/busquedaRepuestos.html", {"mensaje": "no lleno nada"})
# <---------------------------------------------------------------------------------------------------------------------------->
# Mostrar herramienta
@login_required
def leerHerramienta(request):
    herram = Herramienta.objects.all()
    print(herram)
    return render(request, "AppMaquina/leerHerramienta.html", {"herramientas": herram})

# Eliminar herramienta
@login_required
def eliminarHerra(request, id):
    herra = Herramienta.objects.get(id=id)
    herra.delete()
    herra = Herramienta.objects.all()
    return render(request, "AppMaquina/leerHerramienta.html",  {"mensaje": "Herramienta bajada del sistema.", "herramientas": herra} )

# editar o actualizar
@login_required
def editarHerra(request, id):
    herra = Herramienta.objects.get(id=id)
    if request.method == 'POST':
        form = HerraFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)

            herra.nombre = informacion["nombre"]
            herra.cantidad = informacion["cantidad"]
            herra.ubicacion = informacion["ubicacion"]
            herra.save()
            herra = Herramienta.objects.all()
            return render(request, "AppMaquina/leerHerramienta.html", {"mensaje":"herramienta actualizada", "herramientas": herra})
    else:
        formulario = HerraFormulario(initial={"nombre": herra.nombre, "cantiad":herra.cantidad, "ubicacion":herra.ubicacion})
    return render(request, "AppMaquina/editarHerra.html", {"form": formulario, "herramienta":herra})

# <--------------------login----------------------------------------->
def login_request(request):
    if request.method == 'POST':
        form =  AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario1 = form.cleaned_data.get("username")
            clave1 = form.cleaned_data.get("password")

            usuario = authenticate(username = usuario1, password = clave1)
            # trae un usuario de la base, que tenga ese usuario y ese password....
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppMaquina/inicio.html', {'mensaje':f"bienvenido {usuario}"})
            else:
                print("aqui es")
                return render(request, 'AppMaquina/login.html', {'mensaje':"Usuario o contraseña incorrectos"})
        else:
            print("aqui voy")
            return render(request, 'AppMaquina/login.html', {'mensaje':"Usuario o contraseña incorrectos"}) 
           

    else:
        form = AuthenticationForm()
    return render(request, "AppMaquina/login.html", {"form": form})

# registros
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, 'AppMaquina/inicio.html', {'mensaje':"usuario creado correctamente"})
    else:
        form = RegisterForm()
    return render(request, "AppMaquina/register.html", {"form":form})

# logout
# editar usuarios
def editarPerfil(request):
    usuario = request.user
    if request.method=='POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]  
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            print("aca va")

            return render(request, 'AppMaquina/inicio.html', {'mensaje':"usuario Modificado correctamente"})
        else:
            return render(request, 'AppMaquina/inicio.html', {'mensaje':"usuario no se modifico correctamente"})
    else:
        form = UserEditForm(instance = usuario)
        return render(request, "AppMaquina/editarusuario.html", {"form":form, "nombreusuario":usuario.username})




    





