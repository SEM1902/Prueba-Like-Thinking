

from django.test import TestCase
from django.core.exceptions import ValidationError
from domain_layer.models import Empresa

class EmpresaModelTest(TestCase):
    
    def test_crear_empresa_valida(self):
        """Verifica que se pueda crear una empresa con datos válidos"""
        empresa = Empresa(
            nit='123456789',
            nombre='Empresa Test',
            direccion='Calle 123',
            telefono='3001234567'
        )
        empresa.full_clean() # Trigger validation
        empresa.save()
        
        self.assertEqual(empresa.nit, '123456789')
        self.assertEqual(empresa.nombre, 'Empresa Test')
        self.assertIsNotNone(empresa.fecha_creacion)
        self.assertIsNotNone(empresa.fecha_actualizacion)

    def test_validaciones_nit(self):
        """Verifica las validaciones del NIT"""
        # NIT vacío
        empresa = Empresa(nit='', nombre='Test', direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # NIT muy corto
        empresa = Empresa(nit='123', nombre='Test', direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # NIT muy largo
        empresa = Empresa(nit='1234567890123456', nombre='Test', direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # NIT con letras (RegexValidator lo maneja)
        empresa = Empresa(nit='12345678A', nombre='Test', direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_validaciones_nombre(self):
        """Verifica las validaciones del nombre"""
        # Nombre vacío (Django CharField requires blank=False by default)
        empresa = Empresa(nit='123456789', nombre='', direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # Nombre muy largo
        empresa = Empresa(nit='123456789', nombre='A' * 201, direccion='Dir', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_validaciones_direccion(self):
        """Verifica las validaciones de dirección y teléfono"""
        # Dirección vacía
        empresa = Empresa(nit='123456789', nombre='Test', direccion='', telefono='123')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # Teléfono vacío
        empresa = Empresa(nit='123456789', nombre='Test', direccion='Dir', telefono='')
        with self.assertRaises(ValidationError):
            empresa.full_clean()
            
        # Teléfono muy largo
        empresa = Empresa(nit='123456789', nombre='Test', direccion='Dir', telefono='123456789012345678901')
        with self.assertRaises(ValidationError):
            empresa.full_clean()

    def test_actualizar_datos(self):
        """Verifica la actualización de datos"""
        empresa = Empresa.objects.create(
            nit='123456789',
            nombre='Original',
            direccion='Dir Original',
            telefono='111'
        )
        
        # Actualizar campos
        empresa.nombre = 'Nuevo Nombre'
        empresa.direccion = 'Nueva Dir'
        empresa.telefono = '222'
        empresa.save()
        
        empresa.refresh_from_db()
        self.assertEqual(empresa.nombre, 'Nuevo Nombre')
        self.assertEqual(empresa.direccion, 'Nueva Dir')
        self.assertEqual(empresa.telefono, '222')
        
    def test_str_representation(self):
        """Verifica la representación en string"""
        empresa = Empresa(
            nit='123456789',
            nombre='Mi Empresa',
            direccion='Dir',
            telefono='123'
        )
        self.assertEqual(str(empresa), "Mi Empresa - 123456789")
