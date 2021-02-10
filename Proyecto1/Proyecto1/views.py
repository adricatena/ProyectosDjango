from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # Primera vista
    persona1 = Persona("Adriano", "Catena")
    nombre = "Adriano"
    apellido = "Catena"
    #temasDelCurso = []
    temasDelCurso = ["Plantillas", "Modelos",
                     "Formularios", "Vistas", "Deploy"]
    ahora = datetime.datetime.now()
    """ docExterno = open(
        "C:/Users/adria/Documents/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/index.html")
    plantilla = Template(docExterno.read())
    docExterno.close() """
    docExterno = loader.get_template('index.html')
    """ contexto = Context(
        {"nombre_persona": persona1.nombre, "apellido_persona": persona1.apellido, "hora_actual": ahora, "temas": temasDelCurso}) """
    #documento = plantilla.render(contexto)
    documento = docExterno.render({"nombre_persona": persona1.nombre,
                                   "apellido_persona": persona1.apellido, "hora_actual": ahora, "temas": temasDelCurso})
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Hasta luego Django!")


def getFecha(request):
    fechaActual = datetime.datetime.now()
    documento = "<html><body><h1>Fecha y hora actuales: %s</html></body></h1>" % fechaActual
    return HttpResponse(documento)


def calcularEdad(request, edad, anio):
    periodo = anio-2021
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendras %s años</html></body></h2>" % (
        anio, edadFutura)
    return HttpResponse(documento)
