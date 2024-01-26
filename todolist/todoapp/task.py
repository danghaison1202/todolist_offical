# from celery import Celery
# from celery import shared_task
# from django.core.mail import send_mail
# from django.utils import timezone
# from .models import Todo


# @shared_task
# def send_reminder_email(record_id):
#     record = Todo.objects.get(pk=record_id)
#     # Check if the datetime is within the next 24 hours
#     if record.datetime_field - timezone.now() <= timezone.timedelta(days=1):
#         subject = 'Reminder: Complete your To do'
#         message = f"Don't forget to complete your To do: {record.title} at {record.finish_date}."
#         send_mail(subject, message, 'sondangcvta@gmail.com', [record.email])
