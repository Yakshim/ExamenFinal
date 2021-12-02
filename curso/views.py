from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from curso.models import Cursos, Materia

def curso_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            curso = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('alumnos'):
                actuacion = Cursos(actor_id=actor_id, curso_id = curso.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = MateriaForm()
    return render(request, 'curso/curso_nuevo.html', {'formulario': formulario})