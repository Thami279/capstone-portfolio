Quickstart
==========

Follow these steps to set up the Capstone Portfolio project on a fresh
workstation.

Prerequisites
-------------

* Python 3.11 or newer
* virtualenv or `python -m venv`
* Docker Engine (optional, required for container workflow)

Local Environment
-----------------

1. Create and activate a virtual environment::

      python3 -m venv venv
      source venv/bin/activate

2. Install dependencies::

      pip install --upgrade pip
      pip install -r requirements.txt

3. Apply database migrations and start the development server::

      python manage.py migrate
      python manage.py runserver

4. Visit http://127.0.0.1:8000 to view the studio portfolio experience.

Docker Workflow
---------------

1. Build the production image::

      docker build -t capstone-portfolio .

2. Run the container::

      docker run --env DJANGO_SECRET_KEY=changeme --env DJANGO_ALLOWED_HOSTS=localhost \
        -p 8000:8000 capstone-portfolio

3. Navigate to http://127.0.0.1:8000 to interact with the app.

Testing
-------

Execute the automated test suite before shipping changes::

    python manage.py test
