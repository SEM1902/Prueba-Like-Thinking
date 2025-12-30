# Sistema de Gestión de Empresas y Productos

Sistema completo desarrollado con Django, React y PostgreSQL que permite gestionar empresas, productos e inventarios con funcionalidades avanzadas de IA (Google Gemini) y Blockchain.

Este proyecto ha sido re-arquitecturado para seguir **Clean Architecture**, con una capa de dominio separada.

## Características Principales

- ✅ **Gestión de Empresas**: CRUD completo con validaciones
- ✅ **Gestión de Productos**: Productos con precios en múltiples monedas (USD, EUR, COP)
- ✅ **Inventario**: Sistema de inventario por empresa con hash de blockchain
- ✅ **Autenticación JWT**: Sistema de login seguro con contraseñas encriptadas
- ✅ **Roles de Usuario**: Administrador y Externo con permisos diferenciados
- ✅ **Generación de PDFs**: Exportación de inventarios a PDF
- ✅ **Envío de Emails**: Envío de PDFs por correo electrónico
- ✅ **IA Integrada**: Sugerencias de productos, predicciones de stock y chatbot inteligente usando **Google Gemini**
- ✅ **Blockchain**: Hash de transacciones para el inventario
- ✅ **Atomic Design**: Estructura de componentes siguiendo Atomic Design
- ✅ **Clean Architecture**: Lógica de negocio aislada en una capa de dominio independiente

## Tecnologías Utilizadas

### Backend
- Django 4.2.7
- Django REST Framework
- PostgreSQL
- JWT Authentication
- ReportLab (PDFs)
- **Google Gemini API** (IA)
- Web3 (Blockchain)

### Frontend
- React 18.2.0
- React Router DOM
- Axios
- Atomic Design Pattern

## Instalación

### Opción 1: Docker (Recomendado)

#### Prerrequisitos
- Docker
- Docker Compose

#### Pasos

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Prueba
```

2. Construir y levantar los contenedores:
```bash
docker-compose up --build
```

El sistema estará disponible en:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`

### Opción 2: Instalación Manual

#### Prerrequisitos
- Python 3.9+
- Node.js 14+
- PostgreSQL

#### Backend (Django)

1. Crear un entorno virtual y activarlo:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
```

2. Instalar dependencias:
```bash
pip install -r backend/requirements.txt
```

3. Crear archivo `.env` en la carpeta `backend/`:
```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
DB_NAME=postgres
DB_USER=tu_usuario_postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password

# AI Configuration (Google Gemini)
GEMINI_API_KEY=tu_api_key_de_gemini
```

4. Ejecutar migraciones:
**Nota:** Este proyecto usa una app para la capa de dominio (`domain_layer`).
```bash
python backend/manage.py migrate api
python backend/manage.py migrate domain_layer --fake # Si las tablas ya existen
# O si es una instalación limpia:
# python backend/manage.py migrate domain_layer
```

5. Crear superusuario:
```bash
python backend/manage.py createsuperuser
```

6. Iniciar servidor:
```bash
python backend/manage.py runserver
```

#### Frontend (React)

1. Navegar a la carpeta frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Iniciar servidor:
```bash
npm start
```

## Estructura del Proyecto

```
Prueba/
├── domain/                  # [NUEVO] Capa de Dominio Independiente
│   └── src/
│       └── domain_layer/
│           └── models.py    # Entidades de negocio (Empresa, Producto, Inventario)
├── backend/
│   ├── api/                 # Capa de Infraestructura/API
│   │   ├── models.py        # Solo modelo User
│   │   ├── views.py         # Controladores HTTP
│   │   ├── serializers.py   # Adaptadores de datos
│   │   └── services.py      # Servicios externos (IA, Email)
│   ├── config/              # Configuración Django
│   └── manage.py
├── frontend/                # Interfaz de Usuario (React)
└── README.md
```

## Funcionalidades de IA (Google Gemini)

1. **Sugerencias de Productos:** Al ver un producto, la IA sugiere complementarios.
2. **Predicción de Stock:** Analiza el inventario y alerta sobre posibles quiebres de stock.
3. **Chatbot Inteligente:** Responde preguntas en lenguaje natural sobre el estado de tu inventario y empresas.

## Licencia

Este proyecto fue desarrollado como prueba técnica.
