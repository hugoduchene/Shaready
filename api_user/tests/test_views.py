from django.test import TestCase
from user.models import CustomUser
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

class TestUserViews(APITestCase):
    def setUp(self):
        self.user = CustomUser(username="testuser", password="secret123456").save()
        self.research_user_url = reverse("research_user", args=['test'])
        self.create_subscribed_url = reverse("create_subscribed", args=['testuser'])
        self.all_info_user = reverse("all_info_user", args=[10]) #id starts at 10 
        self.data_post_subscribe = {"id_receiving" : 12}

    def test_get_all_info_user(self):
        response = self.client.get(self.all_info_user)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    "image_profile":"user-default.png",
                    "username":"testuser",
                    "info_user":
                    {
                        "nbs_gold_likes":0,"nbs_folows":0
                    }
                }
            ]
        )
    def test_get_research_user(self):
        response = self.client.get(self.research_user_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{"username":"testuser","image_profile":"user-default.png"}]
        )
    
    def test_post_createsubscribe_unauthenticated(self):
        response = self.client.post(
            self.create_subscribed_url,
            self.data_post_subscribe,
            format='json',
        )
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_createsubscribe_aunthenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(
            self.create_subscribed_url,
            self.data_post_subscribe,
            format='json',
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'id_receiving': 12, "nbs_follows" : 1}
        )

