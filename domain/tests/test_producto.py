
import pytest
from decimal import Decimal
from datetime import datetime
from domain_layer.entities.producto import Producto

class TestProducto:
    
    def test_crear_producto_valido(self):
        """Verifica creación de producto válido"""
        producto = Producto(
            codigo='COD001',
            nombre='Producto Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10.0'),
            precio_eur=Decimal('9.0'),
            precio_cop=Decimal('40000.0'),
            empresa_nit='123456789'
        )
        assert producto.codigo == 'COD001'
        assert producto.precio_usd == Decimal('10.0')
        assert producto.empresa_nit == '123456789'

    def test_validaciones_obligatorias(self):
        """Verifica campos obligatorios"""
        base_data = {
            'codigo': 'COD001',
            'nombre': 'Producto Test',
            'caracteristicas': 'Desc',
            'precio_usd': Decimal('10'),
            'precio_eur': Decimal('9'),
            'precio_cop': Decimal('40000'),
            'empresa_nit': '123456789'
        }
        
        # Código vacío
        with pytest.raises(ValueError, match="El código del producto es obligatorio"):
            data = base_data.copy()
            data['codigo'] = ''
            Producto(**data)
            
        # Nombre vacío
        with pytest.raises(ValueError, match="El nombre del producto es obligatorio"):
            data = base_data.copy()
            data['nombre'] = ''
            Producto(**data)
            
        # NIT de empresa vacío
        with pytest.raises(ValueError, match="El producto debe estar asociado a una empresa"):
            data = base_data.copy()
            data['empresa_nit'] = ''
            Producto(**data)

    def test_validaciones_precios_negativos(self):
        """Verifica que no se permitan precios negativos"""
        base_data = {
            'codigo': 'COD001',
            'nombre': 'Test',
            'caracteristicas': 'Desc',
            'precio_usd': Decimal('10'),
            'precio_eur': Decimal('9'),
            'precio_cop': Decimal('40000'),
            'empresa_nit': '123456789'
        }
        
        # USD negativo
        with pytest.raises(ValueError, match="El precio USD no puede ser negativo"):
            data = base_data.copy()
            data['precio_usd'] = Decimal('-1')
            Producto(**data)
            
        # EUR negativo
        with pytest.raises(ValueError, match="El precio EUR no puede ser negativo"):
            data = base_data.copy()
            data['precio_eur'] = Decimal('-1')
            Producto(**data)
            
        # COP negativo
        with pytest.raises(ValueError, match="El precio COP no puede ser negativo"):
            data = base_data.copy()
            data['precio_cop'] = Decimal('-1')
            Producto(**data)

    def test_actualizar_precios(self):
        """Verifica la actualización de precios"""
        producto = Producto(
            codigo='COD001',
            nombre='Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10'),
            precio_eur=Decimal('9'),
            precio_cop=Decimal('40000'),
            empresa_nit='123456789'
        )
        
        producto.actualizar_precios(precio_usd=Decimal('15.0'))
        
        assert producto.precio_usd == Decimal('15.0')
        assert producto.precio_eur == Decimal('9') # No cambió
        assert isinstance(producto.fecha_actualizacion, datetime)
        
        # Error al actualizar con negativo
        with pytest.raises(ValueError, match="El precio USD no puede ser negativo"):
            producto.actualizar_precios(precio_usd=Decimal('-5'))

    def test_actualizar_datos(self):
        """Verifica actualización de datos descriptivos"""
        producto = Producto(
            codigo='COD001',
            nombre='Test',
            caracteristicas='Desc',
            precio_usd=Decimal('10'),
            precio_eur=Decimal('9'),
            precio_cop=Decimal('40000'),
            empresa_nit='123456789'
        )
        
        producto.actualizar_datos(nombre='Nuevo Nombre', caracteristicas='Nueva Desc')
        
        assert producto.nombre == 'Nuevo Nombre'
        assert producto.caracteristicas == 'Nueva Desc'
        assert isinstance(producto.fecha_actualizacion, datetime)
        
        # Validar vacío
        with pytest.raises(ValueError, match="El nombre del producto no puede estar vacío"):
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
            empresa_nit='123456789'
        )
        assert str(producto) == "Test (COD001)"
