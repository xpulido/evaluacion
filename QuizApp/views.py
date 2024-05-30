from django.shortcuts import render
from django.conf import settings
from QuizApp.models import Alumno

def estudiantes(request):
    alumno = Alumno.objects.all()
    return render(request, 'estudiantes.html', {'alumno': alumno})

