class HealthCheckException(Exception):
    pass


class InvalidParams(HealthCheckException):
    pass