from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from personas.models import Personas


# Create your views here.
def bienvenida(request):
    # return HttpResponse('Hola')
    pagina = loader.get_template('Saludos.html')
    return HttpResponse(pagina.render())


def hola(request, nombre):
    apellido = request.GET["apellido"]
    nivel = request.GET["nivel"]
    curso = request.GET["curso"]
    pagina = loader.get_template('Saludos.html')
    nombreCompleto = nombre + " " + apellido
    mensaje = {'nombre': nombreCompleto, 'cursos': curso, 'nivel': nivel}
    return HttpResponse(pagina.render(mensaje, request))


def edad(request, edad):
    pagina = loader.get_template('edad.html')
    mensaje = {'edad': edad}
    return HttpResponse(pagina.render(mensaje, request))


def mostras_personas(resquest):
    cantidad_personas = Personas.objects.count()
    personas = Personas.objects.all().values()

    nombres_Personas = list()
    for persona in personas:
        nombres_Personas.append(persona['Nombre'])

    mensaje = {'cantidad': cantidad_personas, 'personas': personas, 'nombres_Personas': nombres_Personas}
    pagina = loader.get_template('personas.html')
    return HttpResponse(pagina.render(mensaje, resquest))
