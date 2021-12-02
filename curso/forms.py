from django import forms
from .models import Materia,Alumno


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nombre', 'anio', 'alumnos')

    def __init__ (self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Ingrese los alumnos del curso"
        self.fields["alumnos"].queryset = Alumno.objects.all()