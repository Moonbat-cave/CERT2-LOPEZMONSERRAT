from django.db import models

# Create your models here.
class Categoria(models.Model):
    cod = models.CharField(max_length=3, primary_key=True) #Clave Primaria
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre + "(" + self.cod + ")"

class LugarPatrimonial(models.Model):
    cod = models.CharField(max_length=3, primary_key=True) #Clave primaria
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    ubicacion = models.CharField(max_length=100)
    anio_construccion = models.IntegerField()
    imagen = models.URLField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  #Clave foránea a Categoria