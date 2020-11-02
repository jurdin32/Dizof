from django.shortcuts import render

# Create your views here.


from Home.models import Categoria, Proyectos, Principal, Slider, Historia, Equipo, Servicios, Blog, DatosPrincipales


def index(request):
    contexto={
        "sliders":Slider.objects.all(),
        "principal": Principal.objects.last(),
        "equipos":Equipo.objects.all(),
        "servicios":Servicios.objects.all(),
        "historia":Historia.objects.filter(tipo="Historia").first(),
        "pasion":Historia.objects.filter(tipo="Pasion").first(),
        "datosPrincipales":DatosPrincipales.objects.last(),
    }
    return render(request,"index.html",contexto)

def historia(request):
    historias=Historia.objects.filter(tipo="Historia")
    for historia in historias:
        historia.visitas+=1
        historia.save()

    contexto={
        "principal": Principal.objects.last(),
        "historias":historias,
    }
    return render(request,"historia.html",contexto)

def pasion(request):
    historias=Historia.objects.filter(tipo="Pasion")
    for historia in historias:
        historia.visitas+=1
        historia.save()

    contexto={
        "principal": Principal.objects.last(),
        "historias":historias,
    }
    return render(request,"pasion.html",contexto)

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

def blogs(request):
    contexto={
        'blogs':Blog.objects.all().order_by('-id'),
    }
    return render(request,'blog2.html',contexto)

def blog(request,id):
    blog=Blog.objects.get(id=id)
    blog.visitas+=1
    blog.save()
    contexto={
        "blog":blog
    }
    return render(request, 'blog.html', contexto)

