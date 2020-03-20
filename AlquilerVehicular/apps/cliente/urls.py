from django.urls import path
from .import views


urlpatterns = [
 
    path('',views.principalVehiculo),
    path('nuevo_Vehiculo/',views.nuevoVehiculo),
       
]

