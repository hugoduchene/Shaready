from django.db import models
from django.utils import timezone
from user.models import CustomUser

# Create your models here.

class Categories(models.Model):
    name_category = models.CharField(max_length=200)

    
class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    content_article = models.TextField(max_length=850)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_article = models.DateField(default=timezone.now)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class LikeArticle(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gold_like = models.BooleanField(null=True)
    like = models.BooleanField(null=True)
    dislike = models.BooleanField(null=True)
    fuck_like = models.BooleanField(null=True)


class Comment(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_comment = models.DateField(default=timezone.now)
    content_comment = models.TextField(max_length=1000)


class LikeComment(models.Model):
    id_comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like_comment = models.BooleanField(null=True)
    dislike_comment = models.BooleanField(null=True)
