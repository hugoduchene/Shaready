from django.test import TestCase
from user.models import CustomUser
from rest_framework.test import APITestCase
from rest_framework import status
from articles.models import Comment , LikeComment
from django.urls import reverse
from rest_framework.test import APIClient

class TestCommentsEndpoint(APITestCase):
    def setUp(self):
        self.get_all_url = reverse("getAll", args=[0,1])
        self.create_like_comment_url = reverse("create_like_comment", args=[0])
        self.create_comment_url = reverse("Create_comment", args=[0])
        self.data_like_comment = {
            "recation_comment" : 1
        }
        self.data_comment = {
            "content_comment" : "test comment"
        }

    def test_get_all_comment(self):
        response = self.client.get(self.get_all_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_like_comment_unauthenticated(self):
        response = self.client.post(self.create_like_comment_url, self.data_like_comment, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_like_comment_authenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.create_like_comment_url, self.data_like_comment, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_create_comment_article_unauthenticated(self):
        response = self.client.post(self.create_comment_url, self.data_comment, format='json')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_comment_article_authenticated(self):
        user = self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.create_comment_url, self.data_comment, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)