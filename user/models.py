from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from Shaready.settings import ChoicesNotification

# Create your models here.


class CustomUser(AbstractUser):
    image_profile = models.ImageField(upload_to='', default='user-default.png')


class Subscription(models.Model):
    id_receiving = models.ForeignKey(CustomUser, related_name='user_receiving_follow', on_delete=models.CASCADE)
    id_giving = models.ForeignKey(CustomUser, related_name='user_giving_follow', on_delete=models.CASCADE)


class Notification(models.Model):
    id_receiving = models.ForeignKey(CustomUser, related_name='user_receiving_notification', on_delete=models.CASCADE)
    id_giving = models.ForeignKey(CustomUser, related_name='user_giving_notification', on_delete=models.CASCADE)
    type_notification = models.CharField(null=False, max_length=155, choices=ChoicesNotification)
    read = models.BooleanField(default=False)
    date_notification = models.DateTimeField(default=timezone.now)

