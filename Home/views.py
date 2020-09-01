from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class index(TemplateView):
    template_name = "index.html"

class proyectos(TemplateView):
    template_name = "proyectos.html"