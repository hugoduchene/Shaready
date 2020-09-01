from django.test import TestCase, Client
from django.urls import reverse
from articles.models import Article, Categories
from user.models import CustomUser


""" unit test on articles's views """


class TestViews(TestCase):

    def setUp(self):
        CustomUser(username='testUser').save()
        Categories(name_category="TestCategory").save()
        Article(
            title="TestTitle",
            content_article="Test Content",
            id_category=Categories.objects.all()[0],
            id_user=CustomUser.objects.all()[0],
        ).save()
        self.client = Client()
        self.home_url = reverse('home')
        self.feed_url = reverse("feed")
        self.only_article_url = reverse("only_article", args=[Article.objects.all()[0].id])

    def test_get_feed_unauthenticated(self):
        response = self.client.get(self.feed_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_feed_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.feed_url)

        self.assertTemplateUsed(response, 'articles/feed.html')

    def test_get_article_only_unauthenticated(self):
        response = self.client.get(self.only_article_url)

        self.assertRedirects(response, self.home_url, status_code=302)

    def test_get_article_only_authenticated(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.only_article_url)

        self.assertTemplateUsed(response, 'articles/articles_only.html')
