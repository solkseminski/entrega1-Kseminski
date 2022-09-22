
from django.urls import path
from AppWeb.views import *

urlpatterns = [ 
    path("", inicio, name="Inicio"),
    path('cursos/', curso, name="Cursos"),
    path('profesores/', profesor, name="Profesores"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('entregables/', entregable, name="Entregables"),
    path('cursoFormulario', cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"),
    path('estudianteFormulario', estudianteFormulario, name="EstudianteFormulario"),

    path('buscarCamada', busquedaCamada, name="BusquedaCamada"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
]