from django import forms
from .models import Clase, Coach, Alumno

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'