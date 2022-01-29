import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject',  broker='pyamqp://guest@localhost//')

app.config_from_object('djangoProject.settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task_celery_beat': {
        'task': 'hw_niko.tasks.parser',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}
