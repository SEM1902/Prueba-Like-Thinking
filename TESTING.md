# Guía de Pruebas Unitarias

Este documento detalla cómo ejecutar y mantener las pruebas unitarias del proyecto, enfocándose en la **Capa de Dominio**.

## Descripción General

El proyecto utiliza el ejecutor de pruebas estándar de **Django** (`django.test.TestCase`). Las pruebas actuales verifican la integridad de datos, validaciones y lógica de negocio de las entidades principales:
*   **Empresa** (`EmpresaModelTest`)
*   **Producto** (`ProductoModelTest`)
*   **Inventario** (`InventarioModelTest`)

## Ubicación de las Pruebas

Los archivos de prueba se encuentran dentro de la aplicación de dominio:

```
domain/
└── src/
    └── domain_layer/
        └── tests/
            ├── test_empresa.py
            ├── test_inventario.py
            └── test_producto.py
```

## Ejecución de las Pruebas

### 1. Prerrequisitos

Asegúrate de estar en la carpeta raíz del proyecto (`PruebaLT`) y tener activo tu entorno virtual:

```bash
# MacOS / Linux
source venv/bin/activate  
# O si usas .venv
source .venv/bin/activate

# Windows
venv\Scripts\activate
```

### 2. Comando Principal

Para ejecutar todas las pruebas de la capa de dominio, usa el siguiente comando:

```bash
python backend/manage.py test domain_layer
```

### 3. Resultado Esperado

Si todo funciona correctamente, verás una salida similar a esta (ignora los warnings de deprecación de librerías externas):

```text
Found 19 test(s).
Creating test database for alias 'default'...
...................
----------------------------------------------------------------------
Ran 19 tests in 0.043s

OK
Destroying test database for alias 'default'...
```

*   `OK` indica que todas las pruebas pasaron.
*   `FAILED` indicaría que alguna prueba falló, mostrando detalles del error.

## Depuración

*   **ImportError / ModuleNotFoundError**: Asegúrate de que las dependencias estén instaladas (`pip install -r backend/requirements.txt`) y que la estructura de carpetas sea correcta.
*   **Database Error**: Django crea una base de datos de prueba temporal. Asegúrate de que tu usuario de base de datos (configurado en `.env`) tenga permisos para crear bases de datos.

## Agregar Nuevas Pruebas

Para agregar una nueva prueba:
1.  Abre el archivo correspondiente en `domain/src/domain_layer/tests/`.
2.  Crea un nuevo método que comience con `test_` dentro de la clase de prueba.
3.  Usa aserciones como `self.assertEqual()`, `self.assertTrue()` o `self.assertRaises()` para verificar el comportamiento.

Ejemplo:

```python
def test_mi_nueva_funcionalidad(self):
    empresa = Empresa.objects.create(...)
    # ... operaciones ...
    self.assertEqual(empresa.alguna_propiedad, valor_esperado)
```
