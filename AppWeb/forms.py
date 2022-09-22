from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=60)
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    correo = forms.EmailField()
    profesion = forms.CharField(max_length=60)


class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    correo = forms.EmailField()
   
