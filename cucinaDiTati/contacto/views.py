from django import forms
from django.shortcuts import render
from contacto.forms import FormularioContacto

# Create your views here.


def contacto(request):
    formularioContacto = FormularioContacto()
    return render(request, 'contacto/contacto.html', {'formularioContacto': formularioContacto})
