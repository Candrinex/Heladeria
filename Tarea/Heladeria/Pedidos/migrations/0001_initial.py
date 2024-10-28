# Generated by Django 5.1.2 on 2024-10-19 00:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cantidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=200)),
                ('contrasena', models.CharField(max_length=100)),
                ('turno_entrada', models.DateTimeField()),
                ('turno_salida', models.DateTimeField()),
                ('dias_trabaja', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Helado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helado', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Salsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salsa', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.cantidad')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.cliente')),
                ('helado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.helado')),
                ('salsa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.salsa')),
            ],
        ),
    ]