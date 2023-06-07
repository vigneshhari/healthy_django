import redis
from healthy_django.healthcheck.base import HealthCheck


class DjangoCeleryQueueLengthHealthCheck(HealthCheck):

    title = "Cache Check"

    required_params = ["broker", "queue_name", "info_length", "warning_length", "alert_length"]

    def check(self):
        try:
            redis_client = redis.from_url(self.params["broker"])
            queue_length = redis_client.llen(self.params["queue_name"])
            status = 200
            if queue_length < self.params["info_length"]:
                status = 200
            elif queue_length < self.params["warning_length"]:
                status = 300
            elif queue_length < self.params["alert_length"]:
                status = 400
            else:
                status = 500
            return status, {"queue_length": queue_length}
        except BaseException:
            return 500, {}