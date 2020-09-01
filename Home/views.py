from django.shortcuts import render

# Create your views here.


from Home.models import Categoria, Proyectos, Principal


def index(request):
    contexto={
        "principal": Principal.objects.last(),
    }
    return render(request,"index.html",contexto)

def proyectos(request):
    proyectos=Proyectos.objects.all()
    categoria=None
    if request.GET.get("projects"):
        proyectos=Proyectos.objects.filter(categoria=request.GET.get("projects"))
        categoria=Categoria.objects.get(id=request.GET.get("projects"))
    contexto = {
        "categorias":Categoria.objects.all(),
        "proyectos":proyectos.order_by("nombre"),
        "categoria":categoria,
        "principal":Principal.objects.last(),
    }

    return render(request,"proyectos.html",contexto)

