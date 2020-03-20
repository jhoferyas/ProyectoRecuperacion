# Generated by Django 2.2.6 on 2020-03-20 02:22

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
                ('color', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('año', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('alquiler_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=20)),
                ('vehiculo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Cliente')),
                ('Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Vehiculo')),
            ],
        ),
    ]