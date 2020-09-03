from django.db import models

# Create your models here.

class Principal(models.Model):
    logo=models.ImageField(upload_to="logos")
    color_interfaz=models.CharField(default="Verde",
                                    max_length=100,
                                    choices=(
                                        ("/static/css/colors/green.css","Verde"),
                                        ("/static/css/colors/mossgreen.css", "Verde Mostaza"),
                                        ("/static/css/colors/bridge.css", "Verde Claro"),
                                        ("/static/css/colors/orange.css","Naranja"),
                                        ("/static/css/colors/pink.css","Rosado"),
                                        ("/static/css/colors/red.css","Rojo"),
                                        ("/static/css/colors/purple.css","Morado"),
                                        ("/static/css/colors/yellow.css", "Amarillo"),
                                        ("/static/css/colors/violet.css", "Violeta"),
                                        ("/static/css/colors/cyan.css", "Cyan"),
                                        ("/static/css/colors/azul.css", "Azul"),


                                    )
                    )

class Slider(models.Model):
    imagen=models.ImageField(upload_to="Slider")
    frase1=models.CharField(max_length=100)
    posicion_frase1=models.IntegerField(default=50)
    frase2=models.CharField(max_length=100)
    posicion_frase2 = models.IntegerField(default=50)
    texto_decorativo=models.CharField(max_length=100)
    posicion_texto_decorativo = models.IntegerField(default=50)
    izquierda=models.BooleanField(default=True)
    derecha=models.BooleanField(default=False)
    centro=models.BooleanField(default=False)
    duracion=models.IntegerField(default=9)
    text_size=models.IntegerField(default=100)




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
    url=models.URLField(null=True,blank=True)
    autor=models.ForeignKey(Autores, on_delete=models.CASCADE)