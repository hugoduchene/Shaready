from django.test import TestCase
from django.contrib.auth import get_user_model
from articles.models import (
    Categories,
    Article,
    LikeArticle,
    Comment,
    LikeComment,
)

# Create your tests here.

class TestModel(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'TestName',
            password = 'secret',
            email = 'test@gmail.com',
            image_profile = 'test.png',
        )

        self.category = Categories.objects.create(
            name_category = 'TestCategory',
        )

        self.article = Article.objects.create(
            title = 'TestTile',
            content_article = "Test content",
            id_category = self.category,
            id_user = self.user,
        )

        self.likeArticle = LikeArticle.objects.create(
            id_article = self.article,
            id_user = self.user,
            reaction = 'gold_like'
        )

        self.comment = Comment.objects.create(
            id_article = self.article,
            id_user = self.user,
            content_comment = "Test comment"
        )

        self.likeComment = LikeComment.objects.create(
            id_comments = self.comment,
            id_user = self.user,
            reaction_comment = 'like',
        )

    def test_category(self):
        self.assertEquals(self.category.name_category, 'TestCategory')

    def test_article(self):
        self.assertEquals(self.article.content_article, 'Test content')

    def testLikeArticle(self):
        self.assertEquals(self.likeArticle.reaction, 'gold_like')

    def test_comment(self):
        self.assertEquals(self.comment.content_comment, "Test comment")

    def test_LikeComment(self):
        self.assertEquals(self.likeComment.id_user, self.user)
        



