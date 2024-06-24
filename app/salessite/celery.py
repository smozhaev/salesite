import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salessite.settings')

app = Celery('salessite')

app.conf.beat_schedule = {
    'send-message': {
        'task': 'salessite.tasks.send_email_task',
        'schedule': crontab(minute=45, hour=14),
    },
    'store-cache': {
        'task': 'salessite.tasks.store_logging',
        'schedule': crontab(minute='*/20'),
        'args': None
    }
}
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

