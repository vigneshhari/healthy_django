from healthy_django.healthcheck.base import HealthCheck

from django.core.cache import CacheKeyWarning, caches


class DjangoCacheHealthCheck(HealthCheck):

    title = "Cache Check"

    required_params = ["connection_name"]

    def check(self):
        cache = caches[self.params["connection_name"]]
        try:
            cache.set("healthy_django_test", 1)
            if not cache.get("healthy_django_test") == 1:
                raise ValueError("Cache returned wrong value")
            return 200, {}
        except BaseException:
            return 500, {}