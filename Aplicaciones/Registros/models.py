from msilib.schema import Class
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Registros(models.Model):
    placa=models.CharField(primary_key=True,max_length=6)
    fecha=models.DateField()
    tipo_auto=models.CharField(max_length=20)
    valor=models.FloatField()
    costos=models.FloatField()
    arreglos=models.CharField(max_length=100)
