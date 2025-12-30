# Despliegue en Railway (con Base de Datos Neon)

Esta guía te permite desplegar en **Railway** respetando la regla de **cero modificaciones de código**.

## 1. Archivos Agregados
He creado dos archivos de configuración que NO afectan tu lógica pero son necesarios para que Railway reconozca el proyecto Python:
1.  `requirements.txt`: Copia de tus dependencias + `gunicorn` (el servidor web de producción).
2.  `Procfile`: Le dice a Railway cómo encender el servidor.

## 2. Preparar Base de Datos (Neon)

1.  Ve a [Neon.tech](https://neon.tech) y crea tu proyecto.
2.  Obtén la cadena de conexión.
    *   Ejemplo: `postgres://usuario:password@host-name.aws.neon.tech/neondb?sslmode=require`

Como **no modificamos el código** para usar una URL única, debes configurar variable por variable en Railway.

## 3. Despliegue en Railway

1.  Crea una cuenta en [Railway.app](https://railway.app).
2.  **"New Project"** -> **"Deploy from GitHub repo"**.
3.  Selecciona tu repositorio.
4.  Railway detectará Python (gracias a `requirements.txt`).
5.  **ANTES** de que termine el primer deploy (o si falla), ve a la pestaña **Variables** y agrega:

### Variables de Entorno Requeridas

| Variable | Valor | Nota |
| :--- | :--- | :--- |
| `SECRET_KEY` | (Inventa una clave larga) | |
| `DEBUG` | `True` | **Obligatorio** `True` porque no podemos instalar `whitenoise` (regla de no modificar código). Si pones `False`, el Admin se verá sin estilos. |
| `PGSSLMODE` | `require` | **Vital** para conectar con Neon. |
| `DB_NAME` | `neondb` | Nombre por defecto en Neon. |
| `DB_USER` | (Tu usuario de Neon) | |
| `DB_PASSWORD` | (Tu contraseña de Neon) | |
| `DB_HOST` | (Tu host de Neon) | Ej: `ep-xyz.aws.neon.tech` |
| `DB_PORT` | `5432` | |
| `GEMINI_API_KEY` | (Tu API Key) | |

## 4. Migraciones (Base de Datos)

Railway no migra automáticamente. Una vez desplegado:

1.  En el dashboard de Railway, haz clic en tu servicio Django.
2.  Ve a la pestaña **Settings** -> **Build Command**.
3.  Escribe: `python backend/manage.py migrate && python backend/manage.py createsuperuser --noinput || true`
    *   *Nota: Crear superusuario automático requiere configurar variables Django `DJANGO_SUPERUSER_USERNAME`, etc. Si no, hazlo localmente.*

**Método recomendado (Migrar desde local):**
1.  Conecta tu `backend/.env` local a la BD de Neon.
2.  Corre `python backend/manage.py migrate` en tu máquina.
3.  Corre `python backend/manage.py createsuperuser` en tu máquina.
4.  Vuelve a apuntar tu `.env` a `localhost`.

## 5. Verificación
Abre la URL que Railway te generó (ej: `https://web-production-xyz.up.railway.app/api/admin/`).
Deberías ver el Login de Django.
