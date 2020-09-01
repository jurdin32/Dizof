from django.contrib import admin

# Register your models here.
from Home.models import *

admin.site.register(Categoria)
admin.site.register(Autores)
admin.site.register(Proyectos)