from django.shortcuts import render
from .models import Cliente

# Create your views here.

def list_est(request):
    estudiantes = Cliente.objects.all()
    return render(request,"lista.html",{"estudiante":estudiantes})