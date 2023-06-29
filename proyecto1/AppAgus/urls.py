from django.urls import path
from AppAgus.views import inicio, clases, alumnos, profesores,crear_alumno,crear_clase,crear_coach,buscar_alumno,buscar


urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('clases/', clases, name ="clases"),
    path('alumnos/', alumnos, name="alumnos"),
    path('profesores/',profesores, name = "profesores"),
    path('alumnoFormulario/',crear_alumno, name ="crear_alumno"),
    path('claseFormulario/',crear_clase, name ="crear_clase"),
    path('profesorFormulario/',crear_coach, name ="crear_coach"),
    path('busquedaAlumno/', buscar_alumno, name="buscar_alumno"),
    path('resultadoBusqueda/', buscar, name="buscar")

    
]