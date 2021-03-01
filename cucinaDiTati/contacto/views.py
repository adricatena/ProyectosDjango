from django import forms
from django.shortcuts import redirect, render
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    formularioContacto = FormularioContacto()
    if request.method == 'POST':
        formularioContacto = FormularioContacto(data=request.POST)
        if formularioContacto.is_valid:
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            correo = EmailMessage('mensaje desde app Django', 'El usuario con nombre {} y con la direccion {} escribe lo siguiente:\n\n {}'.format(
                nombre, email, mensaje), '', ['adricatena@gmail.com'], reply_to=[email])
            try:
                correo.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'formularioContacto': formularioContacto})
