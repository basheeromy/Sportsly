# myapp/management/commands/startflower.py
from django.core.management.base import BaseCommand
from subprocess import run, PIPE

import time

class Command(BaseCommand):
    help = 'Starts Celery Flower with health check'

    def handle(self, *args, **options):
        """
        Define the command to run Flower.
        """

        cmd = [
            'celery',
            '-A',
            'app',
            'flower',
            '--broker=amqp://rabbitmq_user:rabbitmq_pass@rabbitmq:5672/rabbitmq_vhost',
        ]

        """
        Define a function to check if Celery workers are available.
        """

        def worker_ready():
            result = run(
                ['celery', '-A', 'app', 'inspect', 'ping'],
                stdout=PIPE, stderr=PIPE
            )
            return result.returncode == 0

        """
        Wait for Celery workers to become available.
        """

        while not worker_ready():
            self.stdout.write(
                self.style.SUCCESS('Celery workers not available')
            )
            time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS('Celery workers are available')
        )

        """
        Run Flower with the defined command.
        """

        result = run(cmd, stdout=PIPE, stderr=PIPE)
        self.stdout.write(
            self.style.SUCCESS(
                f'Flower process exited with code {result.returncode}'
            )
        )
