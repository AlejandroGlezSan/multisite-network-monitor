FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependencias del sistema necesarias para psycopg2 y compilación
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar código y ajustar permisos
COPY . .
RUN addgroup --system app && adduser --system --ingroup app app \
    && chown -R app:app /app

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/healthz || exit 1

# En producción setear DJANGO_PRODUCTION=1 y asegurar gunicorn en requirements.txt
CMD ["sh", "-c", "if [ \"$DJANGO_PRODUCTION\" = \"1\" ]; then gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3; else python manage.py runserver 0.0.0.0:8000; fi"]
