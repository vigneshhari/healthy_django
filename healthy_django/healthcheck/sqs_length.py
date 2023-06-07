import boto3
from healthy_django.healthcheck.base import HealthCheck


class AWSSQSQueueHealthCheck(HealthCheck):

    title = "SQS Queue Length Check"

    required_params = ["info_length", "warning_length", "alert_length"]

    def check(self):
        from healthy_django.conf import (
            HEALTHY_DJANGO_AWS_ACCESS_KEY,
            HEALTHY_DJANGO_AWS_REGION,
            HEALTHY_DJANGO_AWS_SECRET,
        )

        try:
            client_args = {
                "region_name": HEALTHY_DJANGO_AWS_REGION,
                "aws_access_key_id": HEALTHY_DJANGO_AWS_ACCESS_KEY,
                "aws_secret_access_key": HEALTHY_DJANGO_AWS_SECRET,
            }
            sqs_client = boto3.resource("sqs", **client_args)
            queue_url = None
            if "queue_url" in self.params:
                queue_url = self.params["queue_url"]
            elif "queue_name" in self.params:
                queue_url = sqs_client.get_queue_url(
                    QueueName=self.params["queue_name"],
                )["QueueUrl"]
            queue = sqs_client.Queue(self.params["queue_url"])
            queue_length = int(queue.attributes["ApproximateNumberOfMessages"])
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
        except BaseException as e:
            print(e)
            return 500, {}