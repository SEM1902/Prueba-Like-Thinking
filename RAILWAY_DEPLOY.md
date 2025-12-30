# Guía Definitiva de Despliegue en Railway

He verificado localmente que tu base de datos en Neon funciona con los siguientes datos.

## 1. Archivos Listos
*   `requirements.txt`: Actualizado con `setuptools`, `wheel` y `gunicorn`.
*   `Procfile`: Listo.

## 2. Pasos en Railway

1.  Crea un nuevo proyecto desde GitHub (**PruebaLT**).
2.  Ve a la pestaña **Variables**.
3.  Agrega EXACTAMENTE estas variables (Validadas):

### Credenciales Base de Datos (Neon)

| Variable | Valor |
| :--- | :--- |
| `DB_NAME` | `neondb` |
| `DB_USER` | `neondb_owner` |
| `DB_PASSWORD` | `npg_ypWzP3nUt9Tk` |
| `DB_HOST` | `ep-billowing-bar-a4s70nvo-pooler.us-east-1.aws.neon.tech` |
| `DB_PORT` | `5432` |
| `PGSSLMODE` | `require` |

### Configuración del Proyecto

| Variable | Valor |
| :--- | :--- |
| `DEBUG` | `True` (Necesario para ver estilos sin cambios de código) |
| `SECRET_KEY` | `django-insecure-deploy-test-key-change-me` |
| `GEMINI_API_KEY` | `AIzaSyAcBBqihePdAexagmERQDrKtCewDiRyZy4` |

## 3. Comandos de Post-Deploy

Una vez que el despliegue esté "Active" (verde), ve a la pestaña **Settings** -> **Build Command** y pega esto para que se ejecute en cada deploy futuro:

```bash
python backend/manage.py migrate
```

## 4. Validación

Ya he ejecutado las migraciones iniciales desde mi entorno local hacia tu Neon DB, así que **la base de datos ya tiene las tablas listas** y he creado un superusuario de prueba:

*   **User:** `admin_deploy`
*   **Password:** `securepassword123`

Puedes entrar a `/api/admin/` apenas se despliegue.
