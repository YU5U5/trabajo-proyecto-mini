from django.db import models

# Create your models here.
class moto(models.Model):
    modelo = models.CharField(max_length= 50)
    tipo_moto = models.CharField(max_length=50)
    cilindrada = models.IntegerField()
    potencia = models.IntegerField()
    precio = models.DecimalField(max_digits= 10, decimal_places= 2)