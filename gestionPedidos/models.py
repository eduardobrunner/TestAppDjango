from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30) #CharField se refiere a que va a contener caracteres
    direccion=models.CharField(max_length=50)
    email=models.EmailField() #obliga a introducir un email valido
    telefono=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField() #obliga a introducir fechas
    entregado=models.BooleanField() #Si o No