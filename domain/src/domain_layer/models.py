from django.db import models
from django.core.validators import RegexValidator

class Empresa(models.Model):
    """Modelo para empresas (Entidad de Dominio)"""
    nit_validator = RegexValidator(
        regex=r'^\d{9,15}$',
        message='El NIT debe contener entre 9 y 15 dígitos'
    )
    
    nit = models.CharField(
        max_length=15,
        primary_key=True,
        validators=[nit_validator],
        verbose_name='NIT'
    )
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la empresa')
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']
        # Mantener compatibilidad con la tabla existente
        db_table = 'api_empresa'
    
    def __str__(self):
        return f"{self.nombre} - {self.nit}"
    

class Producto(models.Model):
    """Modelo para productos (Entidad de Dominio)"""
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    caracteristicas = models.TextField(verbose_name='Características')
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio USD')
    precio_eur = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio EUR')
    precio_cop = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio COP')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='productos', verbose_name='Empresa')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
        # Mantener compatibilidad con la tabla existente
        db_table = 'api_producto'
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Inventario(models.Model):
    """Modelo para inventario de productos por empresa (Entidad de Dominio)"""
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='inventarios', verbose_name='Empresa')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios', verbose_name='Producto')
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    transaccion_hash = models.CharField(max_length=66, blank=True, null=True, verbose_name='Hash de Transacción (Blockchain)')
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        unique_together = ['empresa', 'producto']
        ordering = ['-fecha_ingreso']
        # Mantener compatibilidad con la tabla existente
        db_table = 'api_inventario'
    
    def __str__(self):
        return f"{self.empresa.nombre} - {self.producto.nombre} - Cantidad: {self.cantidad}"
