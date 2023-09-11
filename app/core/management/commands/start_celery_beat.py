from django.core.management.base import BaseCommand
from subprocess import run

class Command(BaseCommand):
    help = 'Starts Celery Beat'

    def handle(self, *args, **options):
        """Define the commands to run Celery Beat."""

        commands = [
            'rm -f ./celerybeat.pid',
            'celery -A app beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler'
        ]

        """Execute the commands."""
        for cmd in commands:
            result = run(cmd, shell=True)
            if result.returncode != 0:
                self.stderr.write(self.style.ERROR(f'Command "{cmd}" failed with exit code {result.returncode}'))
                return

        self.stdout.write(self.style.SUCCESS('Celery Beat started successfully'))
