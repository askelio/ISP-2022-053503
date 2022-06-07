import os

from celery import Celery
from celery.schedules import crontab

# from my_chat import settings
from my_chat.settings import dev_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_chat.settings.dev_settings')

app = Celery('habit_tracker')

app.config_from_object('django.conf:settings.dev_settings', namespace='CELERY')

app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


app.config_from_object(dev_settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-6': {
        'task': 'chat.tasks.send_mail_func',
        'schedule': crontab(hour=6, minute=0)
    }

}

app.autodiscover_tasks()