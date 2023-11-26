from django.shortcuts import render
from .models import Cliente,Empleado,Factura,Registro

def Clientes(request):
    listaso1 = Cliente.objects.all()
    return render(request,"cliente.html", {"clientes":listaso1})

def Empleados(request):
    listado2 = Empleado.objects.all()
    return render(request,"empleados.html", {"empleado":listado2})

def Facturas(request):
    Listado3 = Factura.objects.all()
    return render(request,"facturas.html", {"factura": Listado3})

def Registros(request):
    listado4 = Registro.objects.all()
    return render(request,"registros.html", {"registro":listado4})