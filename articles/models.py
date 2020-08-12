from django.db import models
from django.utils import timezone
from user.models import CustomUser
from Shaready.settings import LikeChoicesArticles, LikeChoicesComment

# Create your models here.

class Categories(models.Model):
    name_category = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name_category

class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    content_article = models.TextField(max_length=850, null=False)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_article = models.DateField(default=timezone.now)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class LikeArticle(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=40, choices=LikeChoicesArticles, null=False)

class Comment(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_comment = models.DateField(default=timezone.now)
    content_comment = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.content_comment

class LikeComment(models.Model):
    id_comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reaction_comment = models.CharField(max_length=40, choices=LikeChoicesComment, null=False)
