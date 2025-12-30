# Guía de Despliegue en Vercel

Este proyecto está configurado para desplegarse en Vercel como un monorepo (Frontend React + Backend Django).

Toma en cuenta que **Vercel es Serverless**, por lo que la base de datos local (PostgreSQL en tu máquina) no funcionará.

## Pasos para Desplegar

### 1. Base de Datos en la Nube
Antes de desplegar, necesitas una base de datos PostgreSQL accesible desde internet.
*   Servicios recomendados (Capa gratuita): **Neon**, **Supabase**, **Railway**.
*   Obtén la URL de conexión (ej: `postgres://user:pass@host:port/dbname`).

### 2. Configuración en Vercel
1.  Sube tu código a **GitHub**.
2.  Entra a [Vercel](https://vercel.com) e importa tu repositorio.
3.  Vercel detectará `vercel.json` y configurará el build automáticamente.
4.  **IMPORTANTE:** Antes de darle a "Deploy", ve a la sección **Environment Variables** y agrega las siguientes variables (usando los datos de tu nueva BD en la nube):

```env
# Variables Obligatorias
SECRET_KEY=tu_clave_secreta_segura
DEBUG=False
GEMINI_API_KEY=tu_api_key_de_google_gemini

# Base de Datos (Cloud)
DB_NAME=nombre_db
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
DB_HOST=host_cloud_db  (ej: ep-xyz.us-east-1.aws.neon.tech)
DB_PORT=5432

# Correo (si usas la función de PDFs)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password
```

### 3. Migraciones
Una vez desplegado, la base de datos en la nube estará vacía. Necesitas ejecutar las migraciones.
Vercel no permite ejecutar comandos shell directamente en las funciones, pero puedes:
1.  Conectarte a tu BD Cloud desde tu computadora local.
2.  Cambiar temporalmente tu `.env` local para apuntar a la BD Cloud.
3.  Ejecutar `python backend/manage.py migrate` desde tu terminal local.
    *   Esto creará las tablas en la nube.
4.  Crear superusuario del mismo modo: `python backend/manage.py createsuperuser`.

### 4. Urls
*   Tu frontend estará en: `https://tu-proyecto.vercel.app`
*   Tu backend responderá en: `https://tu-proyecto.vercel.app/api/...`

## Notas
*   El archivo `vercel.json` incluido en la raíz se encarga de dirigir las peticiones `/api` al backend y el resto al frontend.
*   No se realizaron modificaciones al código fuente del proyecto, solo se agregó configuración de despliegue.
