from django.contrib import admin
from .models import Cliente,Empleado,Factura,Registro

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Factura)
admin.site.register(Registro)