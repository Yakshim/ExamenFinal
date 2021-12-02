from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    alumnos   = models.ManyToManyField(Alumno, through='Cursos')

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cursos = models.ForeignKey(Materia, on_delete=models.CASCADE)

class CursosInLine(admin.TabularInline):
    model = Cursos
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (CursosInLine,)

class MateriaAdmin (admin.ModelAdmin):
    inlines = (CursosInLine,)