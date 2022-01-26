import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject',  broker='pyamqp://guest@localhost//')

app.config_from_object('Celery.settings', namespace='CELERY')

app.autodiscover_tasks()

