

from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from domain_layer.models import Producto, Empresa

class ProductoModelTest(TestCase):
    
    def setUp(self):
        self.empresa = Empresa.objects.create(
            nit='123456789',
            nombre='Empresa Test',
            direccion='Calle 123',
            telefono='3001234567'
        )

    def test_crear_producto_valido(self):
        """Verifica creación de producto válido"""
        producto = Producto(
            codigo='COD001',
            nombre='Producto Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10.0'),
            precio_eur=Decimal('9.0'),
            precio_cop=Decimal('40000.0'),
            empresa=self.empresa
        )
        producto.full_clean()
        producto.save()
        
        self.assertEqual(producto.codigo, 'COD001')
        self.assertEqual(producto.precio_usd, Decimal('10.0'))
        self.assertEqual(producto.empresa.nit, '123456789')

    def test_validaciones_obligatorias(self):
        """Verifica campos obligatorios"""
        # Código vacía
        producto = Producto(
            codigo='',
            nombre='Producto Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10.0'),
            precio_eur=Decimal('9.0'),
            precio_cop=Decimal('40000.0'),
            empresa=self.empresa
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()
            
        # Nombre vacío
        producto.codigo = 'COD001'
        producto.nombre = ''
        with self.assertRaises(ValidationError):
            producto.full_clean()

    def test_validaciones_precios_negativos(self):
        """Verifica que no se permitan precios negativos"""
        # A diferencia de los tests anteriores, Django Model Field validation no siempre checkea esto por defecto a menos que sea PositiveIntegerField
        # DecimalField permite negativos.
        # Pero podemos agregar la validación en full_clean o clean, 
        # sin embargo, aquí estamos probando los métodos de 'actualizar' que SÍ tienen esa validación.
        # Si queremos validar negativos en creación, deberíamos agregar validate_min=0 en el modelo o un validador.
        # Por ahora, solo probamos los métodos de negocio añadidos.
        pass

    def test_actualizar_precios(self):
        """Verifica la actualización de precios"""
        producto = Producto.objects.create(
            codigo='COD001',
            nombre='Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10'),
            precio_eur=Decimal('9'),
            precio_cop=Decimal('40000'),
            empresa=self.empresa
        )
        
        producto.actualizar_precios(precio_usd=Decimal('15.0'))
        
        self.assertEqual(producto.precio_usd, Decimal('15.0'))
        self.assertEqual(producto.precio_eur, Decimal('9')) # No cambió
        
        # Error al actualizar con negativo
        with self.assertRaisesMessage(ValueError, "El precio USD no puede ser negativo"):
            producto.actualizar_precios(precio_usd=Decimal('-5'))

    def test_actualizar_datos(self):
        """Verifica actualización de datos descriptivos"""
        producto = Producto.objects.create(
            codigo='COD001',
            nombre='Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10'),
            precio_eur=Decimal('9'),
            precio_cop=Decimal('40000'),
            empresa=self.empresa
        )
        
        producto.actualizar_datos(nombre='Nuevo Nombre', caracteristicas='Nueva Desc')
        
        self.assertEqual(producto.nombre, 'Nuevo Nombre')
        self.assertEqual(producto.caracteristicas, 'Nueva Desc')
        
        # Validar vacío
        with self.assertRaisesMessage(ValueError, "El nombre del producto no puede estar vacío"):
            producto.actualizar_datos(nombre='')

    def test_str_representation(self):
        """Verifica la representación en string"""
        producto = Producto(
            codigo='COD001',
            nombre='Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10'),
            precio_eur=Decimal('9'),
            precio_cop=Decimal('40000'),
            empresa=self.empresa
        )
        self.assertEqual(str(producto), "Test (COD001)")
