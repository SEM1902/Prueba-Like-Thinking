FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements desde el contexto ROOT
COPY backend/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código de BACKEND y DOMAIN
COPY backend/ /app/backend/
COPY domain/ /app/domain/

# Establecer el directorio de trabajo donde está manage.py
WORKDIR /app/backend

# Asegurar que Python encuentre el módulo domain
ENV PYTHONPATH=/app

# Exponer el puerto
EXPOSE 8000

# Comando para producción con Gunicorn
# Asegurarse de que se recojan los estáticos antes de arrancar
CMD sh -c "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"
