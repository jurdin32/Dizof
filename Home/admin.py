from django.contrib import admin

# Register your models here.
from Dizof.snippers import Attr
from Home.models import *

@admin.register(Categoria)
class AdminCategorias(admin.ModelAdmin):
    list_display_links = Attr(Categoria)
    list_display = Attr(Categoria)

@admin.register(Autores)
class AdminAutores(admin.ModelAdmin):
    list_display_links = Attr(Autores)
    list_display = Attr(Autores)

@admin.register(Proyectos)
class AdminProyectos(admin.ModelAdmin):
    list_display_links = Attr(Proyectos)
    list_display = Attr(Proyectos)

@admin.register(Principal)
class AdminPrincipal(admin.ModelAdmin):
    list_display_links = Attr(Principal)
    list_display = Attr(Principal)

@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display_links = Attr(Slider)
    list_display = Attr(Slider)

@admin.register(Historia)
class AdminHistoria(admin.ModelAdmin):
    list_display_links = Attr(Historia)
    list_display = Attr(Historia)