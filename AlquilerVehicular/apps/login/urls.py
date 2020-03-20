from django.urls import path
from .import views


urlpatterns = [
 
    path('',views.ingresar,name='login'),
    path('cerrar',views.cerrar,name='cerrar_sesion'),

    
]

