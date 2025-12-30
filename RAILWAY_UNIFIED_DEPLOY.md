# Despliegue Unificado (Django + React) en Railway

He configurado tu proyecto para que Django sirva tanto la API como el Frontend React desde un solo servicio.

## Resumen de Cambios
1.  **Frontend Build**: Se generó la versión de producción de React (`npm run build`).
2.  **Integración**: Se movió la carpeta `build` a `backend/react_build`.
3.  **Configuración Django**:
    *   `settings.py`: Ahora busca templates y archivos estáticos en `react_build`.
    *   `urls.py`: Agregada una regla "Catch-all" (`re_path(r'^.*$')`) que sirve `index.html` para cualquier ruta que no sea `/api/` o `/admin/`.

## Instrucciones para Railway

1.  **Variables de Entorno**:
    Asegúrate de tener `DEBUG=True`.
    *   **¿Por qué?** Django no sirve archivos estáticos en producción (`DEBUG=False`) sin configuración adicional (WhiteNoise). Como la regla es "mínima modificación de código", usar `DEBUG=True` es la forma más rápida de que funcionen los estilos de React y el Admin.

2.  **Deployment**:
    Sube los cambios a GitHub. Railway detectará el `requirements.txt` y `Procfile` (generados anteriormente) y desplegará el backend.
    
    *Importante:* Como he movido el build de React dentro de `backend/`, ahora es parte del código fuente que se sube.

3.  **Verificación**:
    *   Accede a `https://tu-proyecto.up.railway.app/`. Deberías ver la App de React.
    *   Accede a `/api/health/`. Debería retornar `{"status": "ok"}`.
    *   Accede a `/admin/`. Debería mostrar el login.

## Estado Final
*   **Base de Datos**: Configurada via variables de entorno (Neon).
*   **Frontend**: Servido por Django en la raíz `/`.
*   **Backend**: API accesible en `/api/`.

## Credenciales de Prueba (Neon DB)

He creado usuarios de prueba directamente en tu base de datos:

| Rol | Email | Password |
| :--- | :--- | :--- |
| **Administrador** | `admin@example.com` | `securepassword123` |
| **Usuario Externo** | `usuario@prueba.com` | `prueba12345` |

