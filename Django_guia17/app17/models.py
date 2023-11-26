from django.db import models

#Creación del modelo que almacena los datos de los clientes
class Cliente(models.Model): 
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f" {self.nombre} {self.apellido}"
     
#Creación del modelo que almacena los datos de los empleados de la empresa
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 
    cargo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="empleados") 
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} | {self.cargo}"
    
#Creación del modelo que almacena los datos de la factura hecha
class Factura(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas") 
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="facturas") 
    
    def __str__(self) -> str:
        return f"Monto: {self.monto} | Cliente: {self.cliente}"

#Creación del modelo que registra los datos de las ventas hechas
class Registro(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="registros") 
    
    def __str__(self) -> str:
        return f"Factura: {self.factura} | fecha: {self.fecha}"