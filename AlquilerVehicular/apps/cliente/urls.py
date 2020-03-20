from django.urls import path
from .import views


urlpatterns = [
 
    path('',views.principalVehiculo, name ='vehiculo'),
    path('nuevo_Vehiculo/',views.nuevoVehiculo),
    path('principalCliente/',views.principalCliente, name ='clientes'),
    path('nuevoalquiler/',views.nuevoalquiler, name ='alquiler'),
    path('reportes/',views.reportes, name ='reportes'),
    path('busqueda/',views.busqueda, name ='busqueda'),
       
]

