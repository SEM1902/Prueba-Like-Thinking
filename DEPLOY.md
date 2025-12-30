# Guía Completa de Despliegue en Vercel (Monorepo Django + React)

Esta guía explica paso a paso cómo desplegar este proyecto (que contiene tanto Backend como Frontend) en un solo proyecto de Vercel.

## 1. Preparar Base de Datos en la Nube
Vercel no aloja bases de datos. Necesitas una externa.

1.  Crea una cuenta gratuita en [Neon.tech](https://neon.tech) o [Railway.app](https://railway.app).
2.  Crea un nuevo proyecto/base de datos PostgreSQL.
3.  Copia la **URL de conexión** (ej: `postgres://usuario:password@host.aws.neon.tech/dbname`).

## 2. Preparar Vercel

1.  Ve a [Vercel](https://vercel.com) e inicia sesión con GitHub.
2.  Haz clic en **"Add New..."** -> **"Project"**.
3.  Importa el repositorio de **PruebaLT**.
4.  **IMPORTANTE:** En la pantalla de configuración ("Configure Project"):
    *   **Framework Preset:** Déjalo en `Other` o `None` (Vercel detectará el `vercel.json`).
    *   **Root Directory:** Déjalo en `./` (la raíz del repositorio). **NO** selecciones `frontend` ni `backend`.

## 3. Variables de Entorno (Environment Variables)

Antes de dar clic en "Deploy", despliega la sección **Environment Variables** y agrega:

| Variable | Valor |
| :--- | :--- |
| `SECRET_KEY` | Una cadena aleatoria larga (ej: `k3y_s3cr3t4_...`) |
| `DEBUG` | `False` |
| `DB_NAME` | (Nombre de tu BD en Neon/Railway) |
| `DB_USER` | (Usuario de tu BD) |
| `DB_PASSWORD` | (Contraseña de tu BD) |
| `DB_HOST` | (Host de tu BD, sin `https://`) |
| `DB_PORT` | `5432` |
| `GEMINI_API_KEY` | Tu API Key de Google Gemini |

*Para el email (opcional):* `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`.

## 4. Desplegar

Haz clic en **Deploy**.

Vercel leerá el archivo `vercel.json` de la raíz, el cual le indica que debe:
1.  Instalar Python y dependencias para el Backend.
2.  Instalar Node.js y construir el Frontend (`npm run build`).

## 5. Solución de Problemas Comunes

### Error 404: NOT_FOUND al abrir la página
Esto suele pasar si la "Ruta de Salida" del frontend no coincide o si Vercel ignora el `vercel.json`.

**Solución 1: Verificar `vercel.json`**
Asegúrate de que el archivo `vercel.json` esté en la RAÍZ del repositorio (junto a `README.md`, no dentro de carpetas).

**Solución 2: Build Command en Vercel**
En los "Settings" del proyecto en Vercel -> **Check Settings** -> **Build & Development Settings**:
*   Asegúrate de que **Output Directory** esté vacío o en default. El `vercel.json` ya se encarga de esto.
*   Si tuviste que cambiar algo, ve a "Deployments" y dale a **Redeploy**.

### La Base de Datos está vacía / Error de conexión
Al desplegar, el código se sube pero la BD está vacía.

**Pasos para migrar la BD en la nube:**
Como no tienes terminal en Vercel, hazlo desde tu PC:

1.  Abre tu archivo local `backend/.env`.
2.  **(Temporalmente)** Cambia los datos de `DB_HOST`, `DB_USER`, etc., por los de tu base de datos en la NUBE (Neon/Railway).
3.  Ejecuta en tu terminal local:
    ```bash
    python backend/manage.py migrate
    python backend/manage.py createsuperuser
    ```
4.  **(Importante)** Vuelve a poner los datos locales en tu `.env` para seguir desarrollando en tu máquina.

## 6. Verificando el Backend
Si el frontend falla, verifica si el backend vive:
Intenta acceder a `https://tu-proyecto.vercel.app/api/admin/`
*   Si carga el login de Django: ¡El backend funciona! El problema es solo visual del frontend.
*   Si da Error 500: Revisa los Logs en el dashboard de Vercel -> Functions.

---
**Nota sobre `vercel.json`:**
El archivo de configuración actual usa el sistema "Legacy Builds" de Vercel porque es la única forma confiable de desplegar Django y React juntos en el mismo repositorio sin configuraciones complejas de Workspaces. Si Vercel te muestra advertencias sobre "Legacy Builds", puedes ignorarlas, seguirá funcionando.
