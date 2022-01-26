from celery import shared_task

from django.core.mail import send_mail as django_send_mail


@shared_task
def send_email(message, receiver):
    django_send_mail(
        subject='Reminder',
        message=f'{message}',
        from_email="test@mail.com",
        recipient_list=[receiver],
    )
