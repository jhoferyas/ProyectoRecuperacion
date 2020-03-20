from django import forms
from apps.modelo.models import Vehiculo

class FormularioVehiculo(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = ["placa","modelo","color","marca","año"]
	
