from django.shortcuts import render, redirect
from .models import Clase, Alumno, Coach
from .forms import ClaseForm, AlumnoForm, CoachForm
from django.db.models import Q
from django.http import HttpResponse


def inicio(request):
    return render(request, "AppAgus/inicio.html")


def clases(request):
    return render(request, "AppAgus/clases.html")

def profesores(request):
    return render(request, "AppAgus/profesores.html")


def alumnos(request):
    return render(request, "AppAgus/alumnos.html")

def cuota(request):
    return render(request, "AppAgus/cuotas.html")




def crear_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppAgus/inicio.html") 

    else:
        form = ClaseForm()

    contexto = {
        'form': form,
    }

    return render(request, 'AppAgus/crear_clase.html', contexto)

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppAgus/inicio.html") 
 

    else:
        form = AlumnoForm()

    contexto = {
        'form': form,
    }

    return render(request, 'AppAgus/crear_alumno.html', contexto)

def crear_coach(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppAgus/inicio.html")  

    else:
        form = CoachForm()

    contexto = {
        'form': form,
    }

    return render(request, 'AppAgus/crear_coach.html', contexto)




def buscar_alumno(request):
    if request.method == 'GET':
        return render(request, 'AppAgus/busquedaAlumno.html')



def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        alumnos = Alumno.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        contexto = {
            'alumnos': alumnos,
            'query': query
        }

        return render(request, 'AppAgus/resultadosBusqueda.html', contexto)
    
    else:
        return HttpResponse("ouch")
    