from django.db import models

class Vehiculo(models.Model):

    vehiculo_id = models.AutoField(primary_key = True)
    placa = models.CharField(max_length=10, null = False)
    modelo = models.CharField(max_length=15, null = False)
    color = models.CharField(max_length=15, null = False)
    marca = models.CharField(max_length=15, null = False)
    año = models.CharField(max_length=15, null = False)


class Cliente(models.Model):

    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=20, null = False, unique = True)
    nombre = models.CharField(max_length=20, null = False)
    Apellido = models.CharField(max_length=20, null = False)
    telefono = models.CharField(max_length=15, null = False)
    direccion = models.CharField(max_length=50, null = False)

class Alquiler(models.Model):

    alquiler_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20, null = False)
    Apellido = models.CharField(max_length=20, null = False)
    vehiculo = models.CharField(max_length=20, null = False)
    color = models.CharField(max_length=20, null = False)
    fechaInicio = models.DateField(auto_now = False, auto_now_add = False, null = False)
    fechaFin = models.DateField(auto_now = False, auto_now_add = False, null = False)  
    Vehiculo = models.ForeignKey(
        'vehiculo',
        on_delete = models.CASCADE,
        )
    def _str_(self):
        string=str(self.nombre)+";"+str(self.alquiler_id)

    Cliente = models.ForeignKey(
        'cliente',
        on_delete = models.CASCADE,
        )
    def _str_(self):
        string=str(self.nombre)+";"+str(self.alquiler_id)    
    

        
    
    
