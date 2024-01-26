from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .task import send_reminder_email
from django.utils import timezone


# Create your models here.
# class Todo(models.Model):
#     title = models.CharField(max_length=1000)
#     # description = models.TextField(max_length=1000)
#     date = models.DateField(auto_now_add = True )

def __str__(self):
        return self.title

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    finish_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

######### Celery config #############

# @receiver(post_save, sender=Todo)
# def schedule_reminder_email(sender, instance, **kwargs):
#     send_reminder_email.apply_async(args=[instance.pk], eta=instance.datetime_field - timezone.timedelta(days=1))
