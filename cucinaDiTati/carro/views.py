from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.


def agregarProducto(request, productoId):
    carro = Carro(request)
    producto = Producto.objects.get(id=productoId)
    carro.agregar(producto=producto)
    return redirect("tienda")


def eliminarProducto(request, productoId):
    carro = Carro(request)
    producto = Producto.objects.get(id=productoId)
    carro.eliminar(producto=producto)
    return redirect("tienda")


def restarProducto(request, productoId):
    carro = Carro(request)
    producto = Producto.objects.get(id=productoId)
    carro.restar(producto=producto)
    return redirect("tienda")


def limpiarCarro(request):
    carro = Carro(request)
    carro.limpiarCarro()
    return redirect("tienda")
