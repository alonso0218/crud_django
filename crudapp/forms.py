from django import forms
from .models import Estudiante 

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields= '__all__'#le indicamos que vamos a trabajr con todos los modelos de la clase estudiante
