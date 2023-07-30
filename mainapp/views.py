from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
def Home(request):

    return render(request, "mainapp/index.html")

def About(request):

    return render(request, "mainapp/about.html")

def Temporadas(request):
    ctx = {"Temporadas": Temporada.objects.all()}

    return render(request, "mainapp/temporadas.html",ctx)

def Personajes(request):
    ctx = {"Personajes": Personaje.objects.all()}

    return render(request, "mainapp/personajes.html", ctx)

def Formulario_Suscripcion(request):
    if request.method == "POST":
        FormSus = Formulario_Suscriptor(request.POST)
        if FormSus.is_valid():
            infoSus = FormSus.cleaned_data
            suscriptor = Suscriptor(nombre=infoSus['nombre'],apellido=infoSus['apellido'],edad=infoSus['edad'],sexo=infoSus['sexo'],direccion=infoSus['direccion'],tarjeta=infoSus['tarjeta'])
            suscriptor.save()
        return render(request, "mainapp/index.html")
    
    else:
        FormSus = Formulario_Suscriptor()
    
    return render(request, "mainapp/formulario_suscripcion.html", {"form": FormSus})

def Formulario_Update_Suscriptor(request,id_suscriptor):
    suscriptor = Suscriptor.objects.get(id=id_suscriptor)
    
    if request.method == "POST":
        formSus = Formulario_Suscriptor(request.POST)
        if formSus.is_valid():
            suscriptor.nombre = formSus.cleaned_data.get('nombre')
            suscriptor.apellido = formSus.cleaned_data.get('apellido')
            suscriptor.direccion = formSus.cleaned_data.get('direccion')
            suscriptor.edad = formSus.cleaned_data.get('edad')
            suscriptor.sexo = formSus.cleaned_data.get('sexo')
            suscriptor.tarjeta = formSus.cleaned_data.get('tarjeta')
            
            suscriptor.save()
            return redirect(reverse_lazy('suscriptores'))
    else:
        formSus = Formulario_Suscriptor(initial={'nombre': suscriptor.nombre, 'apellido': suscriptor.apellido, 'direccion': suscriptor.direccion,'edad': suscriptor.edad, 'sexo': suscriptor.sexo, 'tarjeta':suscriptor.tarjeta})
    
    return render(request, "mainapp/formulario_suscripcion.html", {'form':formSus})

def Delete_Suscriptor(request, id_suscriptor):
    suscriptor = Suscriptor.objects.get(id=id_suscriptor)
    suscriptor.delete()
    return redirect(reverse_lazy('suscriptores'))


def Formulario_Update_Personajes(request,id_personaje):
    personaje = Personaje.objects.get(id=id_personaje)
    
    if request.method == "POST":
        formPersonaje = Formulario_Personajes(request.POST)
        if formPersonaje.is_valid():
            personaje.nombre = formPersonaje.cleaned_data.get('nombre')
            personaje.apellido = formPersonaje.cleaned_data.get('apellido')
            personaje.nombrePersonaje = formPersonaje.cleaned_data.get('nombrePersonaje')
            personaje.apellidoPersonaje = formPersonaje.cleaned_data.get('apellidoPersonaje')
            personaje.save()
            return redirect(reverse_lazy('Personajes'))
    
    else:
        formPersonaje = Formulario_Personajes(initial={'nombre':personaje.nombre, 'apellido': personaje.apellido, 'nombrePersonaje': personaje.nombrePersonaje, 'apellidoPersonaje': personaje.apellidoPersonaje})
    
    return render(request, "mainapp/formulario_personaje.html", {'form':formPersonaje})
            

def Delete_Personaje(request, id_personaje):
    personaje = Personaje.objects.get(id=id_personaje)
    personaje.delete()
    return redirect(reverse_lazy('Personajes'))


def Formulario_Create_Personaje(request):
    if request.method == "POST":
        FormPersonaje = Formulario_Personajes(request.POST)
        if FormPersonaje.is_valid():
            infoPersonaje = FormPersonaje.cleaned_data
            personaje = Personaje(nombre=infoPersonaje['nombre'],apellido=infoPersonaje['apellido'],nombrePersonaje = infoPersonaje['nombrePersonaje'],apellidoPersonaje = infoPersonaje['apellidoPersonaje'])
            personaje.save()
        return render(request, "mainapp/index.html")
    
    else:
        FormPersonaje = Formulario_Personajes()
    
    return render(request, "mainapp/formulario_personaje.html", {"form": FormPersonaje})


def Formulario_Update_Temporada(request,id_temporada):
    temporada = Temporada.objects.get(id=id_temporada)
    
    if request.method == "POST":
        formTemporada = Formulario_Temporada(request.POST)
        if formTemporada.is_valid():
            temporada.nombreTemporada = formTemporada.cleaned_data.get('nombreTemporada')
            temporada.numeroCapitulos = formTemporada.cleaned_data.get('numeroCapitulos')
            temporada.fechaEmision = formTemporada.cleaned_data.get('fechaEmision')
            
            temporada.save()
            return redirect(reverse_lazy('Temporadas'))
    else:
        formTemporada = Formulario_Temporada(initial={'nombreTemporada': temporada.nombreTemporada,'numeroCapitulos': temporada.numeroCapitulos,'fechaEmision': temporada.fechaEmision})
    
    return render(request, "mainapp/formulario_temporadas.html", {'form':formTemporada})

def Delete_Temporada(request, id_temporada):
    temporada = Temporada.objects.get(id=id_temporada)
    temporada.delete()
    return redirect(reverse_lazy('Temporadas'))


def Formulario_Create_Temporada(request):
    if request.method == "POST":
        formTemporada = Formulario_Temporada(request.POST)
        if formTemporada.is_valid():
            infoTemporada = formTemporada.cleaned_data
            temporada = Temporada(nombreTemporada = infoTemporada['nombreTemporada'],numeroCapitulos = infoTemporada['numeroCapitulos'], fechaEmision = infoTemporada['fechaEmision'])
            temporada.save()
        return render(request, "mainapp/index.html")
    
    else:
        formTemporada = Formulario_Temporada()
    
    return render(request, "mainapp/formulario_temporadas.html", {"form": formTemporada})


def Mostrar_Suscriptores(request):

    ctx = {"suscriptores": Suscriptor.objects.all()}

    return render(request, "mainapp/suscriptores.html", ctx)


def Buscar_Personaje(request):
    if request.GET['nombre']:
        nombreBuscar = request.GET['nombre']
        personaje = Personaje.objects.filter(nombre__icontains=nombreBuscar)
        
        return render(request, "mainapp/resultado.html", {"nombre": nombreBuscar,"personaje": personaje})