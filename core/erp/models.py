from django.db import models
from datetime import datetime



class Employee(models.Model):
    names = models.TextField(verbose_name='Nombres')
    document = models.DateField(unique=True, verbose_name='Documento')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    address = models.TextField(verbose_name='Direccion')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    state = models.BooleanField(default=True)
    rol = models.TextField(verbose_name='Rol')
    phone = models.TextField(verbose_name='Telefono')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']

class Client(models.Model):
    names = models.TextField(verbose_name='Nombres')
    surnames = models.TextField(verbose_name='Apellidos')
    document = models.DateField(unique=True, verbose_name='Documento')
    address = models.TextField(null=True, blank=True, verbose_name='Dirección')
    email = models.TextField(null=True, blank= True, verbose_name='email')
    phone = models.TextField(null=True, verbose_name='Telefono')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']


class Sale(models.Model):

    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clien = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.emp.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']
class Product(models.Model):
    codigo = models.DateField(unique=True, verbose_name='codigo')
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    description = models.TextField(verbose_name='Descripcion_products')


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'
        db_table = 'Producto'
        ordering = ['id']

class Sale_product(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    empl = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount_product = models.PositiveIntegerField(verbose_name='Nombres')
    date_sale = models.DateField(default=datetime.now, verbose_name='Fecha de venta')

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'detalle de venta'
        verbose_name_plural = 'detalle de ventas'
        db_table = 'venta_producto'
        ordering = ['id']

class Purchase(models.Model):
    emplo = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_purchase = models.DateField(default=datetime.now, verbose_name='Fecha de compra')

    def __str__(self):
        return self.date_purchase

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compra'
        ordering = ['id']

class Insumo(models.Model):
    name = models.TextField(verbose_name='Nombre_insumo', unique=True)
    amount = models.IntegerField(verbose_name='cantidad')
    measure = models.TextField(verbose_name='unidad de medida')
    date_expiration = models.DateField(verbose_name='fecha de vencimiento', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'insumo'
        verbose_name_plural = 'insumos'
        db_table = 'insumo'
        ordering = ['id']


class Purchase_Insumo(models.Model):
    insu = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    purch = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount_insumo = models.IntegerField(verbose_name='cantidad_insumo')

    def __str__(self):
        return str(self.amount_insumo)

    class Meta:
        verbose_name = 'Compra de insumo'
        verbose_name_plural = 'Compra de insumos'
        db_table = 'comprainsumo'
        ordering = ['id']

class Provider(models.Model):
    names = models.TextField(verbose_name='Nombres')
    document = models.DateField(unique=True, verbose_name='Documento')
    address = models.TextField(null=True, blank=True, verbose_name='Dirección')
    email = models.TextField(null=True, blank=True, verbose_name='email')
    phone = models.TextField(null=True, verbose_name='Telefono')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['id']

class Provider_Insumo(models.Model):
    prov = models.ForeignKey(Provider, on_delete=models.CASCADE)
    insum = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.prov)

    class Meta:
        verbose_name = 'Proveedor de insumo'
        verbose_name_plural = 'Proveedor de insumos'
        db_table = 'proveedor_insumo'
        ordering = ['id']





