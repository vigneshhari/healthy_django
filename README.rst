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

Add list of healthcheck plugins the currently supported plugins along with their spec and settings config.

Add the configs to your settings file as needed

| Django Database Health Check

    Checks if a Database defined in Django is up and running   

Config:

.. code-block:: python

    from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
    ...
    DjangoDatabaseHealthCheck(
        "Database",
        slug="database",
        connection_name="insert_connection_name_here"
    ),
    ...

| Django Cache Health Check

    Checks if a Cache defined in Django is up and running   

Config:

.. code-block:: python

    from healthy_django.healthcheck.django_cache import DjangoCacheHealthCheck
    ...
    DjangoCacheHealthCheck("Cache", slug="cache", connection_name="insert_connection_name_here"),
    ...
        

| Redis based Celery Queue Health Check

    Checks if a Celery queue backlog is within given limits 

Config:

.. code-block:: python

    from healthy_django.healthcheck.celery_queue_length import (
        DjangoCeleryQueueLengthHealthCheck,
    )
    ...
    DjangoCeleryQueueLengthHealthCheck(
        "CeleryQueue",
        slug="celery",
        broker="insert_celery_broker_url_here",
        queue_name="insert_celery_queue_name_to_be_monitored",
        info_length=env.int("CELERY_HEALTH_INFO_LENGTH", default=25),  # Expecting integer data field here
        warning_length=env.int("CELERY_HEALTH_WARN_LENGTH", default=50),  # Expecting integer data field here
        alert_length=env.int("CELERY_HEALTH_ALERT_LENGTH", default=100),  # Expecting integer data field here
    ),
    ...

| AWS SQS Queue Health Check

    Checks if an AWS SQS queue backlog is within given limits     



Access the overall data using a GET request to:

.. code-block:: javascript

    {{http_mode}}://{{domain_name}}/health/

Access the individual data using a GET request to:

.. code-block:: javascript

    {{http_mode}}://{{domain_name}}/health/{{slug}}


Features
--------

| Non ORM Based Database Tests
| RabbitMQ Queue Length Test
| S3 file test


Credits
-------

Made with Love by SecurityAdvisor
