from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_notification_when_task_created(task_title, user_email):
    send_mail(
        subject=f"New Task: {task_title}",
        message=f"Hi, Your task {task_title} was succesfully created.",
        from_email=None,
        recipient_list=[user_email]
    )