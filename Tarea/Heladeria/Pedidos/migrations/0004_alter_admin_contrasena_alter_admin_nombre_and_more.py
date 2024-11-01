# Generated by Django 5.1.2 on 2024-10-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0003_alter_empleado_turno_entrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='contrasena',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cantidad',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contrasena',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='contrasena',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='dias_trabaja',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre_completo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='turno_entrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='turno_salida',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='helado',
            name='helado',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='salsa',
            name='salsa',
            field=models.CharField(max_length=50),
        ),
    ]
