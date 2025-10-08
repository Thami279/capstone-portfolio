# Capstone Portfolio

A production-ready Django portfolio experience showcasing high-impact client work,
complete with automated tests, Sphinx documentation, and a container-first delivery
workflow.

## Quick Start

### Option 1: Docker (Recommended)

1. **Prerequisites**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. **Clone and setup**:
   ```bash
   git clone <your-repo-url>
   cd capstone-portfolio
   cp env.example .env
   ```

3. **Generate secret key**:
   ```bash
   python3 -c "import secrets; print(secrets.token_urlsafe(50))"
   ```
   Copy the output and paste it into `.env` for `DJANGO_SECRET_KEY`

4. **Launch the application**:
   ```bash
   docker compose up --build
   ```

5. **Access the application**:
   - Portfolio: http://127.0.0.1:8000
   - Health check: http://127.0.0.1:8000/health/

### Option 2: Local Development

1. **Prerequisites**: Python 3.11+, PostgreSQL

2. **Setup virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Configure database**:
   - Install PostgreSQL and create a database
   - Update `capstone_portfolio/settings.py` with your database credentials

4. **Run migrations and tests**:
   ```bash
   python manage.py migrate
   python manage.py test
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file with these variables:

```bash
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_DEBUG=False
POSTGRES_DB=capstone
POSTGRES_USER=capstone
POSTGRES_PASSWORD=capstone
```

**Important**: Never commit the `.env` file to version control.

## Testing

Run the test suite:
```bash
# With Docker
docker compose exec web python manage.py test

# Local development
python manage.py test
```

## Documentation

View the generated Sphinx documentation:
- Open `docs/_build/html/index.html` in your browser
- Or rebuild: `cd docs && pip install -r requirements.txt && make html`

## Project Structure

```
capstone-portfolio/
├── capstone_portfolio/     # Django project settings
├── portfolio/             # Main application
├── templates/             # HTML templates
├── static/               # CSS, JS, images
├── docs/                 # Sphinx documentation
├── nginx/                # Nginx configuration
├── Dockerfile            # Container definition
├── docker-compose.yml    # Multi-service orchestration
└── requirements.txt      # Python dependencies
```

## Features

- **Portfolio Management**: Showcase projects, services, and testimonials
- **Contact Form**: Lead capture with validation
- **Responsive Design**: Mobile-first CSS framework
- **Health Monitoring**: `/health/` endpoint for uptime checks
- **Production Ready**: Gunicorn, Nginx, PostgreSQL
- **Comprehensive Testing**: Unit tests for models and views
- **Documentation**: Auto-generated Sphinx docs

## Deployment

For production deployment:

1. **Set strong secrets** in your environment
2. **Configure HTTPS** termination
3. **Use managed database** (AWS RDS, Google Cloud SQL, etc.)
4. **Set up static file storage** (AWS S3, etc.)
5. **Configure monitoring** and logging

## Support

- View documentation in `docs/_build/html/`
- Check logs: `docker compose logs -f`
- Run health check: `curl http://127.0.0.1:8000/health/`