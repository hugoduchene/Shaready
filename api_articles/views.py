from datetime import date
from django.db.models import Count
from django.core.paginator import Paginator
from api_articles.utils.handler_all_data_articles import AllDataArticle
from user.models import CustomUser
from articles.models import Categories, Article, Comment
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Categories, Article, LikeArticle, Comment, LikeComment
from api_articles.serializers import (
    CategoriesSerializer,
    ArticleCreateSerailizer,
    LikeArticleSerializer,
)

""" Manage endpoints articles user """
class GetArticleUser(APIView):
    
    def get(self, request, idUser, idPage):
        get_articles_user = Article.objects.filter(id_user=idUser).order_by('-date_article')
        pagination = Paginator(get_articles_user, 10)
        objects_page = pagination.get_page(idPage).object_list
        serializer = AllDataArticle().get_all_infos(objects_page)

        return Response(serializer.data)

""" Manage endpoint's feed """
class GetArticleTrends(APIView):
    
    def get(self, request, format=None):
        trends_articles = Article.objects.order_by('likearticle').filter(date_article=date.today())[:20]
        
        serializer = AllDataArticle().get_all_infos(trends_articles)
        return Response(serializer.data)

class GetArticleCategory(APIView):

    def get(self, request, idCategory, idPage):
        articles = Article.objects.filter(id_category=idCategory).order_by('-date_article')[:100]
        pagination = Paginator(articles, 10)
        objects_page = pagination.get_page(idPage).object_list
        serializer = AllDataArticle().get_all_infos(objects_page)
        return Response(serializer.data)

""" Manage endpoint's post like's article """

class CreateLikeArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, idArticle):
        serializer = LikeArticleSerializer(data=request.data)
        article = Article.objects.filter(id=idArticle)
        article_is_exist = article.count()
        
        objects_like = LikeArticle.objects.filter(id_user=request.user, id_article=idArticle)
        like_is_exist = objects_like.count()
        
        if article_is_exist > 0:
            if serializer.is_valid():
                if like_is_exist > 0:
                    objects_like.delete()
                    serializer.save(id_article=article[0], id_user=request.user)
                    return Response(serializer.data)
                else:
                    serializer.save(id_article=article[0], id_user=request.user)
                    return Response(serializer.data)
            else:
                return Response("ERROR : serializer n'est pas valide")
        else:
            return Response("ERROR : l'article n'existe pas")


""" Manage endpoint's post article """

class CreateArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = ArticleCreateSerailizer(data=request.data)
        id_category = request.data.get('id_category', '')
        category = Categories.objects.get(id=id_category)

        if serializer.is_valid():
            serializer.save(
                id_user=request.user, 
                date_article=timezone.now(), 
                id_category=category,
            )
            
            return Response(serializer.data)
        else:
            return Response("ERROR SERIALIZER")


""" Manage endpoint's list's user article """

class ListArticlesUser(APIView):
    
    def get(self, request, idUser):
        articles_user = Article.objects.filter(id=idUser)
        serializer = AllDataArticle().get_all_infos(articles_user)
        
        return Response(serializer.data)


""" Manage endpoint's list's categories """

class ListCategories(APIView):

    def get(self, request, format= None):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)

