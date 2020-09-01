from django.test import TestCase
from django.contrib.auth import get_user_model
from user.models import (
    Subscription,
    Notification,
)

""" Unit test on user's model """


class TestModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='TestName',
            password='secret',
            email='test@gmail.com',
            image_profile='test.png',
        )

        self.user_2 = get_user_model().objects.create(
            username='TestName2',
            password='secret2',
            email='test2@gmail.com',
            image_profile='test2.png',
        )

        self.subscription = Subscription.objects.create(
            id_receiving=self.user,
            id_giving=self.user_2,
        )

        self.notification = Notification.objects.create(
            id_receiving=self.user,
            id_giving=self.user_2,
            type_notification='comments',
        )

    def test_user(self):
        self.assertEquals(self.user.username, 'TestName')

    def test_subscription(self):
        self.assertEquals(self.subscription.id_receiving, self.user)

    def test_notification(self):
        self.assertEquals(self.notification.type_notification, 'comments')
