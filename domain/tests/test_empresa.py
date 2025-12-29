
import pytest
from datetime import datetime
from domain_layer.entities.empresa import Empresa

class TestEmpresa:
    
    def test_crear_empresa_valida(self):
        """Verifica que se pueda crear una empresa con datos válidos"""
        empresa = Empresa(
            nit='123456789',
            nombre='Empresa Test',
            direccion='Calle 123',
            telefono='3001234567'
        )
        assert empresa.nit == '123456789'
        assert empresa.nombre == 'Empresa Test'
        assert empresa.direccion == 'Calle 123'
        assert empresa.telefono == '3001234567'
        assert empresa.fecha_creacion is None
        assert empresa.fecha_actualizacion is None

    def test_validaciones_nit(self):
        """Verifica las validaciones del NIT"""
        # NIT vacío
        with pytest.raises(ValueError, match="El NIT es obligatorio"):
            Empresa(nit='', nombre='Test', direccion='Dir', telefono='123')
            
        # NIT muy corto
        with pytest.raises(ValueError, match="El NIT debe contener entre 9 y 15 dígitos"):
            Empresa(nit='123', nombre='Test', direccion='Dir', telefono='123')
            
        # NIT muy largo
        with pytest.raises(ValueError, match="El NIT debe contener entre 9 y 15 dígitos"):
            Empresa(nit='1234567890123456', nombre='Test', direccion='Dir', telefono='123')
            
        # NIT con letras
        with pytest.raises(ValueError, match="El NIT debe contener solo dígitos"):
            Empresa(nit='12345678A', nombre='Test', direccion='Dir', telefono='123')

    def test_validaciones_nombre(self):
        """Verifica las validaciones del nombre"""
        # Nombre vacío
        with pytest.raises(ValueError, match="El nombre de la empresa es obligatorio"):
            Empresa(nit='123456789', nombre='', direccion='Dir', telefono='123')
            
        # Nombre muy largo
        with pytest.raises(ValueError, match="El nombre de la empresa no puede exceder 200 caracteres"):
            Empresa(nit='123456789', nombre='A' * 201, direccion='Dir', telefono='123')

    def test_validaciones_direccion(self):
        """Verifica las validaciones de dirección y teléfono"""
        # Dirección vacía
        with pytest.raises(ValueError, match="La dirección es obligatoria"):
            Empresa(nit='123456789', nombre='Test', direccion='', telefono='123')
            
        # Teléfono vacío
        with pytest.raises(ValueError, match="El teléfono es obligatorio"):
            Empresa(nit='123456789', nombre='Test', direccion='Dir', telefono='')
            
        # Teléfono muy largo
        with pytest.raises(ValueError, match="El teléfono no puede exceder 20 caracteres"):
            Empresa(nit='123456789', nombre='Test', direccion='Dir', telefono='123456789012345678901')

    def test_actualizar_datos(self):
        """Verifica la actualización de datos"""
        empresa = Empresa(
            nit='123456789',
            nombre='Original',
            direccion='Dir Original',
            telefono='111'
        )
        
        # Actualizar todos los campos
        empresa.actualizar_datos(
            nombre='Nuevo Nombre',
            direccion='Nueva Dir',
            telefono='222'
        )
        
        assert empresa.nombre == 'Nuevo Nombre'
        assert empresa.direccion == 'Nueva Dir'
        assert empresa.telefono == '222'
        assert isinstance(empresa.fecha_actualizacion, datetime)

    def test_actualizar_datos_parcial(self):
        """Verifica la actualización parcial de datos"""
        empresa = Empresa(
            nit='123456789',
            nombre='Original',
            direccion='Dir Original',
            telefono='111'
        )
        
        empresa.actualizar_datos(nombre='Solo Nombre')
        
        assert empresa.nombre == 'Solo Nombre'
        assert empresa.direccion == 'Dir Original'
        assert empresa.telefono == '111'
        assert isinstance(empresa.fecha_actualizacion, datetime)

    def test_error_actualizar_datos_invalidos(self):
        """Verifica errores al actualizar con datos inválidos"""
        empresa = Empresa(
            nit='123456789',
            nombre='Original',
            direccion='Dir Original',
            telefono='111'
        )
        
        with pytest.raises(ValueError, match="El nombre de la empresa no puede estar vacío"):
            empresa.actualizar_datos(nombre='')
            
        with pytest.raises(ValueError, match="La dirección no puede estar vacía"):
            empresa.actualizar_datos(direccion='')
            
        with pytest.raises(ValueError, match="El teléfono no puede estar vacío"):
            empresa.actualizar_datos(telefono='')
            
    def test_str_representation(self):
        """Verifica la representación en string"""
        empresa = Empresa(
            nit='123456789',
            nombre='Mi Empresa',
            direccion='Dir',
            telefono='123'
        )
        assert str(empresa) == "Mi Empresa - 123456789"
