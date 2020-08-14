from user.models import CustomUser
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TestNotificationViews(APITestCase):
    def setUp(self):
        self.nbs_notif_url = reverse("nbs_notif")
        self.post_notif_read_url = reverse("post_notif_read")
        self.get_all_notif_url = reverse("get_all_notif", args=[1])

    def test_get_nbs_notif_unauthenticated(self):
        response = self.client.get(self.nbs_notif_url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_get_nbs_notif_authenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.nbs_notif_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_notif_read_unauthenticated(self):
        response = self.client.post(self.post_notif_read_url, "", format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_post_notif_read_aunthenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.post_notif_read_url, "", format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_get_all_notif_unauthenticated(self):
        response = self.client.get(self.get_all_notif_url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_all_notif_authenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.get_all_notif_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        