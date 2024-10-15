from django.db import models
from django.conf import settings
from django.utils import timezone 
# Create your models here.
#Tipos:5
#Modificadores:5
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50,blank=True)
    SEXO=[("M","Masculino"),("F","Femenino")]
    sexo=models.CharField(max_length=1,choices=SEXO)
    fechaNacimiento=models.DateField()
    codigoPostal=models.IntegerField()
    domicilio=models.TextField()
    correo= models.EmailField(max_length=50)
    telefono=models.PositiveIntegerField()
    dni=models.CharField(max_length=9,unique=True)

class Local(models.Model):
    precio=models.FloatField()
    metros=models.DecimalField(decimal_places=3)
    anioArrendamiento=models.DateField()
    
class EstacionItv(models.Model):
    id_local=models.OneToOneField(Local,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,unique=True)
    munipio=models.CharField(max_length=50)
    eficiencia_energetica=models.CharField(max_length=1)
    
class Cita(models.Model):
    id_cliente=models.ManyToOneRel(Cliente,)