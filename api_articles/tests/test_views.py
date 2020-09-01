from user.models import CustomUser
from rest_framework.test import APITestCase
from rest_framework import status
from articles.models import Categories
from django.urls import reverse

""" Manages unit tests on feed endpoints """


class TestFeedEndpoint(APITestCase):

    def setUp(self):
        self.article_subscribed_url = reverse("get_articles_sub", args=[1])
        self.trends_artcle_url = reverse("trends")
        self.article_category_url = reverse("list_artcile_category", args=[3, 1])
        self.article_user_url = reverse("article_user", args=[1, 1])

    def test_get_article_sub_unautenticated(self):
        response= self.client.get(self.article_subscribed_url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_article_sub_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response= self.client.get(self.article_subscribed_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_article_user(self):
        response = self.client.get(self.article_user_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_trends_api(self):
        response = self.client.get(self.trends_artcle_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_article_category(self):
        response = self.client.get(self.article_category_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


""" Manages the unit tests on the likes of articles """


class TestPostLikeEndpoint(APITestCase):

    def setUp(self):
        self.user = CustomUser(username="testUser", password="secret123456")
        self.user.save()
        self.create_like_article_url = reverse("create_like_article", args=[1, 'testuser'])
        self.data_like_article = {
            "reaction": 1
        }

    def test_post_create_like_article_unaunthenticated(self):

        response = self.client.post(
            self.create_like_article_url,
            self.data_like_article
        )
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_like_article_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.create_like_article_url, self.data_like_article, format='json')

        self.assertEquals(response.status_code, 400)


""" Manages unit tests on the creation of articles """


class TestCreateArticle(APITestCase):

    def setUp(self):
        self.user = CustomUser(username="testUser", password="secret123456")
        self.user.save()
        self.create_article_url = reverse("create_article")
        self.categories = Categories.objects.get_or_create(id=64)
        self.data_article = {
            "title": "testTile",
            "content_article": "test content",
            "id_category": 64
        }

    def test_post_create_article_unauthenticate(self):
        response = self.client.post(self.create_article_url, self.data_article)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_article_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.create_article_url, self.data_article, format='json')
        self.assertEquals(response.status_code, 200)


""" Manages the unit tests on the item list according to the user """


class TestListUser(APITestCase):

    def setUp(self):
        self.list_article_url = reverse("list_article_user", args=[1])

    def test_get_list_user(self):
        response = self.client.get(self.list_article_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


""" Manages unit tests on the list of categories """


class TestListCategories(APITestCase):

    def setUp(self):
        self.list_categories_url = reverse("categories_api")

    def test_get_list_categories(self):
        response = self.client.get(self.list_categories_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
