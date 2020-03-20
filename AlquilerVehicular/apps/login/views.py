from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import FormularioLogin
from django.contrib.auth  import authenticate, login, logout

def ingresar(request):
	if request.method=='POST':
		formulario=FormularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']#no se usa cleaned data xq no hay formulario
			clave = request.POST['password']
			user = authenticate(username = usuario, password = clave)#reviso que sea usuario
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse("name"))#peticion de respueta
				else:
					print("usuario desactivado")
			else:
				messages.info(request, 'Usurio y/o contrasea Invalidas')
				print("usuario y/o contraseña invalida")
			
	else:
		formulario=FormularioLogin()

	context={
		'formulario':formulario,
		}
    
	return render(request,'login/login.html',context)
	
def cerrar(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

