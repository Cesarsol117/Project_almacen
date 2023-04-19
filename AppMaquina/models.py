from django.db import models

# Create your models here.
class Herramienta(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+ str(self.cantidad)+" "+ self.ubicacion

class Insumos(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    fecha_vence = models.DateField()


    def __str__(self) -> str:
        return self.nombre+" "+ str(self.cantidad) +" "+ self.ubicacion+" "+ str(self.fecha_vence)

class Repuestos(models.Model):
    nombre = models.CharField(max_length=50)
    maquina = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre+" "+ self.maquina+" "+ str(self.cantidad)+" "+ self.ubicacion


class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.nombre+" "+ self.email
      
    