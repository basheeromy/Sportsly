"""This file is to setup celery for this project."""

import os

from celery import Celery

from celery.schedules import crontab


from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker='amqp://rabbitmq_user:rabbitmq_pass@rabbitmq:5672/rabbitmq_vhost')

app.conf.result_backend = 'db+postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(
    USER=os.environ.get('DB_USER'),
    PASSWORD=os.environ.get('DB_PASS'),
    HOST=os.environ.get('DB_HOST'),
    PORT=os.environ.get('DB_PORT', '5432'),  # Default PostgreSQL port is 5432
    NAME=os.environ.get('DB_NAME'),
)
app.conf.broker_connection_retry_on_startup = True
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {


}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)

def debug_task(self):
    print(f"Request: {self.request!r}")

if __name__ == '__main__':
    app.start()