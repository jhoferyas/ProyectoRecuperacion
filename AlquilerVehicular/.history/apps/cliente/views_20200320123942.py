from django.contrib import messages
from django.http import HttpResponseRedirect, jsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from apps.modelo.models import Vehiculo, Cliente, Alquiler
from .forms import FormularioVehiculo

def principalVehiculo(request):
    lista = Vehiculo.objects.all()
    context = {
        'lista' : lista
    }

    usuario = request.user
    if usuario.groups.filter(name = 'Administrador').exists():
        return render(request, "vehiculos/principal_vehiculos.html",context)   

    elif usuario.groups.filter(name = 'empleado').exists():
        return render(request, "vehiculos/principal_vehiculos.html",context)   

    messages.info(request, 'Inicie Sesion Primero')
    return HttpResponseRedirect (reverse('login'))


def nuevoVehiculo(request):
    formularioI = FormularioVehiculo(request.POST)
    usuario = request.user
    if usuario.groups.filter(name = 'Administrador').exists():
        if request.method == 'POST':
                if formularioI.is_valid():
                    
                    datosc = formularioI.cleaned_data  #obteniendo todos los datos del formulario cuenta
                    vehiculo = Vehiculo() #creo objeto en la clase cuenta
                    vehiculo.placa = datosc.get('placa')
                    vehiculo.modelo = datosc.get('modelo')
                    vehiculo.color = datosc.get('color')
                    vehiculo.marca = datosc.get('marca')
                    vehiculo.año = datosc.get('año')
                    vehiculo.save()
                    messages.info(request, 'Registrado Exitosamente!!')
                    return redirect(principalVehiculo)          
    
    elif usuario.groups.filter(name = 'empleado').exists():
        messages.info(request, 'El Empleado no puede Agregar Vehiculos!!')
        return redirect(principalVehiculo)
    
    context = {
        'f': formularioI, 
    }
    

    return render(request, "vehiculos/nuevo_vehiculo.html",context)    



def principalCliente(request):
    lista = Cliente.objects.all()
    context = {
        'listac' : lista
    }

    usuario = request.user
    if usuario.groups.filter(name = 'Administrador').exists():
        return render(request, "clientes/principal_clientes.html",context)   

    elif usuario.groups.filter(name = 'empleado').exists():
        return render(request, "clientes/principal_clientes.html",context)   

    messages.info(request, 'Inicie Sesion Primero')
    return HttpResponseRedirect (reverse('login'))


def reportes(request):
    listaal = Alquiler.objects.all()
    context = {
        'listaal' : listaal
    }

    usuario = request.user
    if usuario.groups.filter(name = 'gerente').exists():
        return render(request, "reportes/reportes.html",context)   

    messages.info(request, 'Inicie Sesion Primero')
    return HttpResponseRedirect (reverse('login'))



def nuevoalquiler(request):
    usuario = request.user
    if usuario.groups.filter(name = 'Administrador').exists():
        messages.info(request, 'El Administrador no puede realizar Alquileres')
        return render(request, "vehiculos/principal_vehiculos.html")   

    elif usuario.groups.filter(name = 'empleado').exists():
        return render(request, "reportes/nuevoAlquiler.html")    

    messages.info(request, 'El Administrador no puede realizar Alquileres')
    return HttpResponseRedirect (reverse('login'))
        

def busqueda(request):
    
    
    return jsonResponse 
    
