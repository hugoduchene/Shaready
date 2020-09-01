from django.urls import path
from api_notification.views import (
    NbsNotification,
    ManageNotification,
    GetAllNotification,
)

urlpatterns = [
    path('getnbsnotifications', NbsNotification.as_view(), name="nbs_notif"),
    path('postmanagenotification', ManageNotification.as_view(), name="post_notif_read"),
    path('getallnotification/<int:idPage>', GetAllNotification.as_view(), name="get_all_notif"),
]
