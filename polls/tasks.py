from celery import shared_task

from django.core.mail import send_mail as django_send_mail

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('tasks',  broker='pyamqp://guest@localhost//')

app.config_from_object('Celery.settings', namespace='CELERY')

app.autodiscover_tasks()


@shared_task
def send_email(message, receiver):
    django_send_mail(
        subject='Напоминание',
        message=f'{message}',
        from_email="test@mail.com",
        recipient_list=[receiver],
    )
