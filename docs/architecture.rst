Architecture Overview
=====================

The Capstone Portfolio project demonstrates a production-friendly Django
architecture optimised for storytelling-driven marketing sites.

Application Layers
------------------

* **Presentation** — Class-based views and templates render curated content
  slices while keeping the experience fast and accessible.
* **Domain** — Django models capture services, projects, testimonials, and
  inbound leads with reusable querysets that power the UI metrics.
* **Interaction** — Forms provide defensive validation to guard against
  low-quality submissions while keeping the experience frictionless.

Static Assets
-------------

A lightweight Tailwind-inspired stylesheet lives in ``static/css/styles.css`` and
is served via Django's staticfiles framework. ``collectstatic`` will populate the
``staticfiles`` directory at build time.

Observability
-------------

``settings.py`` is configured with a console logger that can be extended to send
structured logs to a log aggregation platform in production.

Extensibility
-------------

* Add new sections by creating additional templates and updating
  ``HomePageView.get_context_data``.
* Integrate a CMS by swapping the Django ORM models with an API client layer
  while reusing the existing forms and views.
* Replace the SQLite database with PostgreSQL by updating the ``DATABASES``
  setting and injecting credentials via environment variables or Docker secrets.
