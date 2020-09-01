from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50, help_text="NO mas de 50 Caracteres")

    def __str__(self):
        return self.nombre

class Autores(models.Model):
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=60)
    imagen=models.FileField(upload_to="projects/")
    url=models.URLField()
    autor=models.ForeignKey(Autores, on_delete=models.CASCADE)