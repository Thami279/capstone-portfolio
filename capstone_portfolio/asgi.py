"""ASGI config for the Capstone Portfolio project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_portfolio.settings")

application = get_asgi_application()
