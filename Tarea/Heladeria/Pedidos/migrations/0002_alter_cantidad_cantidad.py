# Generated by Django 5.1.2 on 2024-10-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantidad',
            name='cantidad',
            field=models.CharField(max_length=100),
        ),
    ]