from django import forms
from django.shortcuts import redirect, render
from contacto.forms import FormularioContacto

# Create your views here.


def contacto(request):
    formularioContacto = FormularioContacto()
    if request.method == 'POST':
        formularioContacto = FormularioContacto(data=request.POST)
        if formularioContacto.is_valid:
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            return redirect('/contacto/?valido')

    return render(request, 'contacto/contacto.html', {'formularioContacto': formularioContacto})
