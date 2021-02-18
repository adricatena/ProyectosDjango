from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.


def busquedaProductos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["producto"]:
        #mensaje = "Articulo buscado: %r" % request.GET["producto"]
        producto = request.GET['producto']
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        return render(request, 'resultados_busqueda.html', {"articulos": articulos, 'query': producto})
    else:
        mensaje = "No has introducido nada a buscar"
    return HttpResponse(mensaje)
