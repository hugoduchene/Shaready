from django.contrib import admin
from user.models import CustomUser, Subscription, Notification

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Subscription)
admin.site.register(Notification)
