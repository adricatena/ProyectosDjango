from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'ProyectoWebApp/home', {'nombre': 'home'})


def servicios(request):
    return render(request, 'ProyectoWebApp/servicios', {'nombre': 'servicios'})


def tienda(request):
    return render(request, 'ProyectoWebApp/tienda')


def blog(request):
    return render(request, 'ProyectoWebApp/blog')


def contacto(request):
    return render(request, 'ProyectoWebApp/contacto')
