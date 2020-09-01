from django.shortcuts import render

# Create your views here.


from Home.models import Categoria, Proyectos


def index(request):
    return render(request,"index.html")

def proyectos(request):
    proyectos=Proyectos.objects.all()
    categoria=None
    if request.GET.get("projects"):
        proyectos=Proyectos.objects.filter(categoria=request.GET.get("projects"))
        categoria=Categoria.objects.get(id=request.GET.get("projects"))
    contexto = {
        "categorias":Categoria.objects.all(),
        "proyectos":proyectos,
        "categoria":categoria,
    }

    return render(request,"proyectos.html",contexto)

