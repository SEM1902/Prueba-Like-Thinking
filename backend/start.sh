#!/bin/bash
set -e

echo "🚀 [START.SH] Iniciando script de arranque..."

echo "📦 [START.SH] Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "📦 [START.SH] Aplicando migraciones..."
python manage.py migrate

echo "💾 [START.SH] Cargando datos iniciales..."
python manage.py loaddata db_data.json

echo "👤 [START.SH] Ejecutando script de usuarios de prueba..."
python create_test_users.py

echo "🔥 [START.SH] Iniciando Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
