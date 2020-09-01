from utils.notification import ManageNotification
from user.models import CustomUser, Notification
from django.test import TestCase

""" unit test on notification """


class TestManageNotification(TestCase):

    def setUp(self):
        self.user = CustomUser(username="testuser", password="secret123456")
        self.user.save()

    def test_create_notification(self):
        ManageNotification().create_notification(self.user, "testuser", 1)
        notif_is_exist = Notification.objects.all().count()

        self.assertEquals(notif_is_exist, 1)
