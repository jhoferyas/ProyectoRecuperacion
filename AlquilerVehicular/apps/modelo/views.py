from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index (request):
   usuario = request.user
   if usuario.groups.filter(name = 'Administrador').exists():
      print(usuario)
      return render(request,'principal/index.html')   

   elif usuario.groups.filter(name = 'empleado').exists():
      print(usuario)
      return render(request,'principal/index.html')

   elif usuario.groups.filter(name = 'gerente').exists():
      print(usuario)
      return render(request,'principal/principalgerente.html')      

   print("HOLI")
   messages.info(request, 'Inicie Sesion Primero')
   return HttpResponseRedirect (reverse('login'))
