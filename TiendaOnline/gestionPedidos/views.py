from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import formularioContacto

# Create your views here.


def busquedaProductos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["producto"]:
        #mensaje = "Articulo buscado: %r" % request.GET["producto"]
        producto = request.GET['producto']
        if len(producto) > 20:
            mensaje = 'Texto de busqueda demasiado largo'
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados_busqueda.html', {"articulos": articulos, 'query': producto})
    else:
        mensaje = "No has introducido nada a buscar"
    return HttpResponse(mensaje)


def contacto(request):
    if request.method == 'POST':
        miFormulario = formularioContacto(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            send_mail(informacion['asunto'], informacion['mensaje'], informacion.get(
                'email', ''), ['adricatena@gmail.com'])
            return render(request, 'gracias.html')
    else:
        miFormulario = formularioContacto()
    return render(request, 'formulario_contacto.html', {'form': miFormulario})

    # if request.method == 'POST':
    #     subject = request.POST['asunto']
    #     message = request.POST['mensaje'] + ' ' + request.POST['email']
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ['adricatena@gmail.com']
    #     send_mail(subject, message, email_from, recipient_list)
    #     return render(request, 'gracias.html')
    # else:
    #     return render(request, 'contacto.html')
