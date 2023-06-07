from healthy_django.healthcheck.base import HealthCheck

from django.db import connections
from django.db.utils import OperationalError


class DjangoDatabaseHealthCheck(HealthCheck):

    title = "Database Check"

    required_params = ["connection_name"]

    def check(self):
        db_conn = connections[self.params["connection_name"]]
        try:
            c = db_conn.cursor()
            c.execute("select 1")
            connected = c.fetchone()[0] == 1
            if not connected:
                raise ConnectionError
            return 200, {}
        except OperationalError:
            return 500, {}
        except BaseException:
            return 503, {}