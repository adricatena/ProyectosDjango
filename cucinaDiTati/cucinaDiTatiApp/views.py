from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'cucinaDiTatiApp/home.html')


def tienda(request):
    return render(request, 'cucinaDiTatiApp/tienda.html')


def contacto(request):
    return render(request, 'cucinaDiTatiApp/contacto.html')
