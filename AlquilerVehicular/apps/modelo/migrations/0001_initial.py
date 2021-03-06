# Generated by Django 2.2.6 on 2020-03-20 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('vehiculo_id', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=15)),
                ('color', models.CharField(choices=[('rojo', 'rojo'), ('verde', 'verde'), ('Amarillo', 'Amarillo'), ('Blanco', 'Blanco'), ('Gris', 'Gris'), ('Cafe', 'Cafe'), ('Negro', 'Negro'), ('Rosa', 'Rosa'), ('morado', 'morado'), ('magenta', 'magenta'), ('naranja', 'naranja')], default='rojo', max_length=15)),
                ('marca', models.CharField(choices=[('Toyota', 'Toyota'), ('Mercedes', 'Mercedes'), ('BMW', 'BMW'), ('Honda', 'Honda'), ('Ford', 'Ford'), ('Nissan', 'Nissan'), ('Tesla', 'Tesla'), ('Audi', 'Audi'), ('Volkswagen', 'Volkswagen'), ('Porsche', 'Porsche')], default='Toyota', max_length=15)),
                ('año', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')], default='2000', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('alquiler_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('placa_vehiculo', models.CharField(max_length=20)),
                ('fechaInicio', models.CharField(max_length=20)),
                ('fechaFin', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Cliente')),
                ('Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Vehiculo')),
            ],
        ),
    ]
