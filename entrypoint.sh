#!/bin/sh
set -e

mkdir -p "${DJANGO_STATIC_ROOT:-/app/staticfiles}" "${DJANGO_MEDIA_ROOT:-/app/media}"

python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn capstone_portfolio.wsgi:application --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3}
