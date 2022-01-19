from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from floppyforms import RegexField


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nota = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(10)], decimal_places=2, max_digits=4)
    pagina_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Evaulacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    puntuacion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha.__str__() + self.proveedor.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)
    poblacion = models.CharField(max_length=50)
    telefono = RegexField(regex=r'^\+?1?\d{9,15}$', error_message="Lo introducido no es un número de telefono válido")

    def __str__(self):
        return self.nombre


class Analisis(models.Model):
    nombre = models.CharField(max_length=100)
    factura = models.FileField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre