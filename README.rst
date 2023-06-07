=============================
healthy_django
=============================

Simple Re Usable tool for Django Healthchecks

Documentation
-------------


Quickstart
----------

Install healthy_django::

    pip install healthy_django

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'healthy_django',
        ...
    )

Add healthy_django's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path("health/", include("healthy_django.urls", namespace="healthy_django")),
        ...
    ]

Add list of healthcheck plugins the currently supported plugins along with their spec

| Django Database Health Check

    Checks if a Database defined in Django is up and running    

| Django Cache Health Check

    Checks if a Cache defined in Django is up and running    

| Redis based Celery Queue Health Check

    Checks if a Celery queue backlog is within given limits 

| AWS SQS Queue Health Check

    Checks if an AWS SQS queue backlog is within given limits     


Features
--------

| Non ORM Based Database Tests
| RabbitMQ Queue Length Test
| S3 file test


Credits
-------

Made with Love by SecurityAdvisor