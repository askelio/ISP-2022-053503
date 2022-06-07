from email.message import Message
from urllib import request
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.dispatch import receiver
from my_chat.settings.dev_settings import EMAIL_HOST_USER
from .models import *
import datetime


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    # movies = Movie.objects.filter(draft=False, date_creation__gte=date_from)
    mail_subject = "habits"
    for user in users:
        # count = Message.objects.filter(receiver = user.username)
        to_email = 'gogolyadza@gmail.com'
        message = f"You recived {3} new messages today!"
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return "Done"