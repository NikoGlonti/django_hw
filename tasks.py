# from django.core.mail import send_mail as django_send_mail
# from celery import shared_task
#
#
# @shared_task
# def send_email(message, receiver):
#     django_send_mail(
#         subject='Напоминание',
#         message=f'{message}',
#         from_email="test@mail.com",
#         recipient_list=[receiver],
#     )
