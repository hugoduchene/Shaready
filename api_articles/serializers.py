from articles.models import Categories
from rest_framework import serializers
from articles.models import (
    Article,
    Categories,
    LikeArticle,
    Comment,
    LikeComment,
)


class LikeArticleSerializer(serializers.ModelSerializer):
    nbs_likes = serializers.SerializerMethodField()

    def get_nbs_likes(self, obj):
        return obj.nbs_likes
    
    class Meta:
        model = LikeArticle
        fields = ('reaction', 'nbs_likes')

class ArticleCreateSerailizer(serializers.ModelSerializer):
    info_user = serializers.SerializerMethodField()

    def get_info_user(self, obj):
        return obj.info_user
    
    class Meta:
        model = Article
        fields = ('title', 'content_article', 'id_category', 'info_user')

class ArticleSerializer(serializers.ModelSerializer):
    nbs_likes = serializers.SerializerMethodField()
    info_user = serializers.SerializerMethodField()
    
    def get_nbs_likes(self, obj): 
        return obj.nbs_likes
    
    def get_info_user(self, obj):
        return obj.info_user

    class Meta:
        model = Article
        fields ='__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'