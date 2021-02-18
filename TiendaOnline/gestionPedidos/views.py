from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def busquedaProductos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    mensaje = "Articulo buscado: %r" % request.GET["producto"]
    return HttpResponse(mensaje)
