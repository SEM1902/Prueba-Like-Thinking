# Configuración de Docker

Este proyecto está completamente dockerizado y listo para ejecutarse con Docker Compose.

## Estructura Docker

- **docker-compose.yml**: Configuración principal con 3 servicios:
  - `db`: Base de datos PostgreSQL
  - `backend`: Aplicación Django
  - `frontend`: Aplicación React

- **backend/Dockerfile**: Imagen Docker para el backend
- **frontend/Dockerfile**: Imagen Docker para el frontend

## Configuración Inicial

1. **Crear archivo .env en backend/**:
```bash
cp backend/.env.example backend/.env
```

2. **Editar backend/.env** con tus configuraciones:
```env
SECRET_KEY=tu-secret-key-aqui
DB_NAME=prueba_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-password
GEMINI_API_KEY=tu-gemini-api-key
```

**Nota**: `DB_HOST=db` es importante porque en Docker el servicio de base de datos se llama `db`.

## Comandos Principales

### Iniciar el proyecto
```bash
docker-compose up --build
```

### Detener el proyecto
```bash
docker-compose down
```

### Ver logs
```bash
docker-compose logs -f
```

### Ejecutar migraciones
```bash
docker-compose exec backend python manage.py migrate
```

### Crear superusuario
```bash
docker-compose exec backend python manage.py createsuperuser
```

### Ejecutar comandos Django
```bash
docker-compose exec backend python manage.py <comando>
```

### Reconstruir contenedores
```bash
docker-compose down
docker-compose up --build
```

## Puertos

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- PostgreSQL: `localhost:5432`

## Volúmenes

Los datos de PostgreSQL se persisten en un volumen Docker llamado `postgres_data`.

Para eliminar completamente los datos:
```bash
docker-compose down -v
```

## Desarrollo

Los archivos están montados como volúmenes, por lo que los cambios en el código se reflejan automáticamente sin necesidad de reconstruir los contenedores.

