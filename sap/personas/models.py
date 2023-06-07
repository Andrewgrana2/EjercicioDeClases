from django.db import models

# Create your models here.
class Personas (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Activo = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id} - {self.Nombre} {self.Apellido}'


