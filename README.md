# Capstone Portfolio

A production-ready Django portfolio showcasing client work with a container-first workflow, automated tests, and Sphinx documentation.

## Prerequisites

- Python 3.12+
- Docker and Docker Compose (for container workflow)
- Node.js is **not** required

Clone the repository or download the ZIP:

```bash
git clone https://github.com/Thami279/capstone-portfolio.git
cd capstone-portfolio
```

## Local Development (venv)

1. Create and activate a virtual environment.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. Prepare the database and run the automated tests.
   ```bash
   python manage.py migrate
   python manage.py test
   ```
3. Start the development server.
   ```bash
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/`.

## Environment Configuration

Copy the example file and adjust values before running in production:

```bash
cp env.example .env
```

Set at minimum:
- `DJANGO_SECRET_KEY`: generate with `python -c "import secrets; print(secrets.token_urlsafe(50))"`
- `DJANGO_ALLOWED_HOSTS`: comma-separated hostnames (e.g. `127.0.0.1,localhost`)
- `DATABASE_URL`: optional, defaults to SQLite for local development
- `DJANGO_DEBUG`: `True` for local debugging, `False` for production

Never commit `.env` or secrets; `.gitignore` already excludes them.

## Documentation

Sphinx sources live in `docs/` and the generated HTML output is tracked in `docs/_build/html`.

```bash
sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html  # macOS (optional)
```

If Sphinx is not available globally, install it into the active virtual environment:

```bash
pip install -r docs/requirements.txt
```

## Docker Workflow

1. Copy environment defaults then set production-ready values.
   ```bash
   cp env.example .env
   ```
2. Build and run the stack (Django + Gunicorn, PostgreSQL, Nginx):
   ```bash
   docker compose up --build
   ```
3. Wait until the `web` container reports that migrations ran successfully, then visit `http://127.0.0.1:8000`.

To run management commands inside the container:

```bash
docker compose exec web python manage.py <command>
```

Persistent Docker volumes:
- `postgres_data`: PostgreSQL data files
- `static_data`: collected static assets
- `media_data`: uploaded media

## Testing

```bash
python manage.py test
```

For containerised tests:

```bash
docker compose exec web python manage.py test
```

## Deployment Checklist

- Configure production database credentials and allowed hosts in `.env`.
- Collect static files with `python manage.py collectstatic`.
- Provision HTTPS for Nginx and update container environment variables.
- Set up health checks (e.g. `/health/`) if required by your hosting provider.

## Repository Notes

- Documentation is maintained on the `docs` branch and merged into `main`.
- Docker support lives on the `container` branch and is merged into `main`.
- The public repository URL is stored in `capstone.txt`.
