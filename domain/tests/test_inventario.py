
import pytest
from datetime import datetime
from domain_layer.entities.inventario import Inventario

class TestInventario:
    
    def test_crear_inventario_valido(self):
        """Verifica creación de inventario válido"""
        inv = Inventario(
            empresa_nit='123456789',
            producto_codigo='COD001',
            cantidad=100
        )
        assert inv.empresa_nit == '123456789'
        assert inv.producto_codigo == 'COD001'
        assert inv.cantidad == 100

    def test_validaciones_init(self):
        """Verifica validaciones iniciales"""
        # NIT vacío
        with pytest.raises(ValueError, match="El inventario debe estar asociado a una empresa"):
            Inventario(empresa_nit='', producto_codigo='COD', cantidad=10)
            
        # Código producto vacío
        with pytest.raises(ValueError, match="El inventario debe estar asociado a un producto"):
            Inventario(empresa_nit='123', producto_codigo='', cantidad=10)
            
        # Cantidad negativa
        with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
            Inventario(empresa_nit='123', producto_codigo='COD', cantidad=-1)

    def test_actualizar_cantidad(self):
        """Verifica actualización de cantidad"""
        inv = Inventario('123', 'COD', 10)
        
        inv.actualizar_cantidad(20)
        assert inv.cantidad == 20
        assert isinstance(inv.fecha_actualizacion, datetime)
        
        # Error negativo
        with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
            inv.actualizar_cantidad(-5)

    def test_incrementar_cantidad(self):
        """Verifica incremento de cantidad"""
        inv = Inventario('123', 'COD', 10)
        
        inv.incrementar_cantidad(5)
        assert inv.cantidad == 15
        
        # Error incremento negativo
        with pytest.raises(ValueError, match="El incremento no puede ser negativo"):
            inv.incrementar_cantidad(-1)

    def test_decrementar_cantidad(self):
        """Verifica decremento de cantidad"""
        inv = Inventario('123', 'COD', 10)
        
        inv.decrementar_cantidad(3)
        assert inv.cantidad == 7
        
        # Error decremento negativo
        with pytest.raises(ValueError, match="El decremento no puede ser negativo"):
            inv.decrementar_cantidad(-1)
            
        # Error saldo insuficiente
        with pytest.raises(ValueError, match="La cantidad resultante no puede ser negativa"):
            inv.decrementar_cantidad(20)

    def test_establecer_hash_transaccion(self):
        """Verifica establecer hash de transacción"""
        inv = Inventario('123', 'COD', 10)
        
        hash_tx = "0x123abc"
        inv.establecer_hash_transaccion(hash_tx)
        assert inv.transaccion_hash == hash_tx
        
        # Validar vacío
        with pytest.raises(ValueError, match="El hash de transacción no puede estar vacío"):
            inv.establecer_hash_transaccion('')
            
        # Validar longitud
        with pytest.raises(ValueError, match="El hash de transacción no puede exceder 66 caracteres"):
            inv.establecer_hash_transaccion('a' * 67)

    def test_str_representation(self):
        """Verifica la representación en string"""
        inv = Inventario(
            empresa_nit='123',
            producto_codigo='COD',
            cantidad=50
        )
        expected = "Empresa: 123 - Producto: COD - Cantidad: 50"
        assert str(inv) == expected
