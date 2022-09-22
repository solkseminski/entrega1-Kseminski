from django.shortcuts import render, loader
from django.http import HttpResponse

from AppWeb.forms import *
from .models import *
# Create your views here.


def inicio(request):

    return render(request,"AppWeb/inicio.html")



def curso(request):

    cur1 = Curso(nombre="python", camada=41635)
    cur1.save() 

    return render(request,"AppWeb/curso.html")


def estudiante(request):

    return render(request,"AppWeb/estudiantes.html")


def profesor(request):

   return render(request,"AppWeb/profesores.html")


def entregable(request):

   return render(request,"AppWeb/entregables.html")


def cursoFormulario(request):

    if request.method == "POST":
        miformulario= CursoFormulario(request.POST)
        print(miformulario) 
       
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data 
            curso= Curso (nombre = informacion['curso'], camada=informacion['camada'])
            curso.save() 

            return render(request, "AppWeb/inicio.html") 

    else: 
        miformulario=CursoFormulario()

    return render(request, "AppWeb/cursoFormulario.html", {"miformulario":miformulario})
   



def profesorFormulario(request):

    if request.method == "POST":
        miformulario= ProfesorFormulario(request.POST)
        print(miformulario)
       
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data 
            profesor= Profesor (nombre = informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], profesion=informacion['profesion'])
            profesor.save() 
 
            return render(request, "AppWeb/inicio.html") 

    else: 
        miformulario=ProfesorFormulario()

    return render(request, "AppWeb/profesorformulario.html", {"miformulario":miformulario})


def estudianteFormulario(request):

    if request.method == "POST":
        miformulario= EstudianteFormulario(request.POST)
        print(miformulario)
       
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data 
            estudiante= Estudiante (nombre = informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'],)
            estudiante.save() 

            return render(request, "AppWeb/inicio.html") 

    else: 
        miformulario=EstudianteFormulario() 

    return render(request, "AppWeb/estudianteFormulario.html", {"miformulario":miformulario})


def busquedaCamada(request):
    return render(request, "AppWeb/inicio.html")

def buscar(request):

    if request.GET["camada"]:
        camada=request.GET["camada"]
        cursos=Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppWeb/resultadosbusqueda.html", {"cursos":cursos, "camada":camada})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def resultados(request):

    if request.GET["camada"]:
        camada= request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppWeb/inicio.html", {"cursos":cursos, "camada":camada})

    else:
        respuesta = "No enviaste Datos"

    return HttpResponse(respuesta)




