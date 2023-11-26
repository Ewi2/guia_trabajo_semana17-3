from django.db import models


class Cliente(models.Model): 
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"nombre: {self.nombre} apellido: {self.apellido} tipo de cliente:{self.tipo} dirección: {self.direccion}"
     

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 
    cargo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="empleados") 
    
    def __str__(self) -> str:
        return f"nombre: {self.nombre} apellido: {self.apellido} cargo: {self.cargo} dirección: {self.cargo} cliente: {self.cliente}"
    

class Factura(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas") 
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="facturas") 
    
    def __str__(self) -> str:
        return f"monto: {self.monto} impuesto: {self.impuesto} estado: {self.estado} cliente: {self.cliente} empleado: {self.empleado}"


class Registro(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="registros") 
    
    
    def __str__(self) -> str:
        return f"tipo: {self.tipo} fecha: {self.fecha} factura: {self.factura}"