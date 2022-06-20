from django.core.mail import send_mail
from celery.utils.log import get_task_logger

from uchet import settings
from uchet.celery import app

logger = get_task_logger(__name__)


@app.task(name="send_email_task")
def send_email_task(recipient):
    """sends an email when task field changed"""
    send_mail(subject='Subject task status changed.',
              message='Message task status changed.',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[recipient])
