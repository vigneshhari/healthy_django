from healthy_django.healthcheck.django_cache import DjangoCacheHealthCheck
from django.conf import settings
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from healthy_django.healthcheck.celery_queue_length import DjangoCeleryQueueLengthHealthCheck
from healthy_django.healthcheck.sqs_length import AWSSQSQueueHealthCheck

default_configuration = []

HEALTH_CHECK = getattr(settings, "HEALTHY_DJANGO", default_configuration)
HEALTHY_DJANGO_AWS_REGION = getattr(settings, "HEALTHY_DJANGO_AWS_REGION", None)
HEALTHY_DJANGO_AWS_ACCESS_KEY = getattr(settings, "HEALTHY_DJANGO_AWS_ACCESS_KEY", None)
HEALTHY_DJANGO_AWS_SECRET = getattr(settings, "HEALTHY_DJANGO_AWS_SECRET", None)
