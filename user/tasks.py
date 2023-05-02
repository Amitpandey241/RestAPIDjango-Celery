from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def send_mail_task(email):
    send_mail(
        "Registration Sucessfull",
        "You have Been Register",
        "ap7788546@gmail.com",
        [email],
        fail_silently=False,
    )
    print("MAIL FROM CELERY")
    return None
