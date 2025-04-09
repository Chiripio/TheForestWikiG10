from django.db import models

class RolUsuario(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(RolUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
