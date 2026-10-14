from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    valor = models.PositiveIntegerField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.cliente} - {self.equipo.nombre}"
