from utils.all_data_article import AllDataArticle
from utils.all_data_comment import AllDataComment
from django.test import TestCase
from articles.models import Categories, Article, Comment
from user.models import CustomUser

""" unit test on all data article """


class TestAllDataArticle(TestCase):

    def setUp(self):
        CustomUser(username="TestUser").save()
        Categories(name_category="TestCategory").save()
        Article(
            title="TestTitle",
            content_article="Test Content",
            id_category=Categories.objects.all()[0],
            id_user=CustomUser.objects.all()[0],
        ).save()
        Comment(
            id_article=Article.objects.all()[0],
            id_user=CustomUser.objects.all()[0],
            content_comment="test comment",
        ).save()
        self.all_data_article = AllDataArticle()
        self.all_data_comment = AllDataComment()
        self.obj_article = Article.objects.all()
        self.obj_comment = Comment.objects.all()

    def test_get_all_infos(self):
        serializer = self.all_data_article.get_all_infos(self.obj_article)

        self.assertEquals(len(serializer.data[0]), 9)

    def test_get_all_infos_comment(self):
        serializer = self.all_data_comment.get_all_infos_comment(self.obj_comment)

        self.assertEquals(len(serializer.data[0]), 7)
