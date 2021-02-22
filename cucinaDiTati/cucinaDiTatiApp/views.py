from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.


def home(request):
    return render(request, 'cucinaDiTatiApp/home.html')


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'cucinaDiTatiApp/servicios.html', {'servicios': servicios})


def tienda(request):
    return render(request, 'cucinaDiTatiApp/tienda.html')


def contacto(request):
    return render(request, 'cucinaDiTatiApp/contacto.html')


def blog(request):
    return render(request, 'cucinaDiTatiApp/blog.html')
