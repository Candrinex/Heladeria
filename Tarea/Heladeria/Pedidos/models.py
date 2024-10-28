from django.db import models
import json

DIAS_CHOICES = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
]

class Admin(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario

class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    turno_entrada = models.TimeField()
    turno_salida = models.TimeField()
    dias_trabaja = models.JSONField()  # Aquí usamos JSONField para almacenar varios días

    def __str__(self):
        return self.nombre_completo

class Helado(models.Model):
    helado = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # Guardamos el color en formato hexadecimal

    def __str__(self):
        return self.helado

class Cantidad(models.Model):
    cantidad = models.CharField(max_length=50)

    def __str__(self):
        return str(self.cantidad)

class Salsa(models.Model):
    salsa = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # Guardamos el color en formato hexadecimal

    def __str__(self):
        return self.salsa

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    helado = models.ForeignKey(Helado, on_delete=models.CASCADE)
    salsa = models.ForeignKey(Salsa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido de {self.cliente} - Helado: {self.helado}, Cantidad: {self.cantidad}, Salsa: {self.salsa}"
