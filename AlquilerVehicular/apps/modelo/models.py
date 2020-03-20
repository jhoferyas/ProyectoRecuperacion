from django.db import models

class Vehiculo(models.Model):

    listacolor = (
        ('rojo','rojo'),
        ('verde','verde'),
        ('Amarillo','Amarillo'),
        ('Blanco','Blanco'),
        ('Gris','Gris'),
        ('Cafe','Cafe'),
        ('Negro','Negro'),
        ('Rosa','Rosa'),
        ('morado','morado'),
        ('magenta','magenta'),
        ('naranja','naranja'),
    )

    listamarca = (
        ('Toyota','Toyota'),
        ('Mercedes','Mercedes'),
        ('BMW','BMW'),
        ('Honda','Honda'),
        ('Ford','Ford'),
        ('Nissan','Nissan'),
        ('Tesla','Tesla'),
        ('Audi','Audi'),
        ('Volkswagen','Volkswagen'),
        ('Porsche','Porsche'),
    )

    listaaño = (
        ('2000','2000'),
        ('2001','2001'),
        ('2002','2002'),
        ('2003','2003'),
        ('2004','2004'),
        ('2005','2005'),
        ('2006','2006'),
        ('2007','2007'),
        ('2008','2008'),
        ('2009','2009'),
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
    )

    vehiculo_id = models.AutoField(primary_key = True)
    placa = models.CharField(max_length=10, null = False)
    modelo = models.CharField(max_length=15, null = False)
    color = models.CharField(max_length=15, null = False, choices= listacolor, default='rojo')
    marca = models.CharField(max_length=15, null = False, choices= listamarca, default='Toyota')
    año = models.CharField(max_length=15, null = False, choices= listaaño, default='2000')


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
    placa_vehiculo = models.CharField(max_length=20, null = False)
    fechaInicio = models.CharField(max_length=20, null = False)
    fechaFin = models.CharField(max_length=20, null = False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null= False)
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

    def _str(self):
        string=str(self.nombre)+";"+str(self.alquiler_id)    
    

        
    
    
