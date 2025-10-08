"""Sphinx configuration for the Capstone Portfolio project documentation."""

from __future__ import annotations

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_portfolio.settings")

import django  # noqa: E402

django.setup()

project = "Capstone Portfolio"
author = "Capstone Studio"
current_year = datetime.now().strftime("%Y")
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]
html_title = "Capstone Portfolio Documentation"

# Autodoc settings ensure expressive docstrings render beautifully.
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_typehints = "description"

napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/stable", None),
}

rst_epilog = f".. |year| replace:: {current_year}"
