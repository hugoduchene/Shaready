from datetime import date
from rest_framework import status
from django.db.models import Count
from utils.notification import ManageNotification
from utils.all_data_article import AllDataArticle
from user.models import CustomUser, Subscription
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from articles.models import Categories, Article, LikeArticle
from api_articles.serializers import (
    CategoriesSerializer,
    ArticleCreateSerailizer,
    LikeArticleSerializer,
)

""" Manage endpoints articles user """


class GetArticleUser(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, idUser, idPage):
        get_articles_user = Article.objects.filter(id_user=idUser).order_by('-date_article')
        serializer = AllDataArticle().get_all_infos(AllDataArticle().pagination_objects(get_articles_user, idPage))
        return Response(serializer.data)


""" Manages subscription endpoints """


class GetArticleSubscribed(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, idPage):
        user_subscribed = Subscription.objects.filter(id_giving=request.user)
        list_id = [i.id_receiving for i in user_subscribed]
        articles = Article.objects.filter(id_user__in=list_id).order_by('-date_article')[:100]
        serializer = AllDataArticle().get_all_infos(AllDataArticle().pagination_objects(articles, idPage))
        return Response(serializer.data)


""" Manages trend endpoints """


class GetArticleTrends(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        trends_articles = Article.objects.filter(date_article=date.today()).annotate(
            count=Count('likearticle')
        ).order_by('-count')[:20]

        serializer = AllDataArticle().get_all_infos(trends_articles)
        return Response(serializer.data)


""" Manages item categories """


class GetArticleCategory(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, idCategory, idPage):
        articles = Article.objects.filter(id_category=idCategory).order_by('-date_article')[:100]
        serializer = AllDataArticle().get_all_infos(AllDataArticle().pagination_objects(articles, idPage))
        return Response(serializer.data)


""" Manage endpoint's post like's article """


class CreateLikeArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, idArticle, pseudoUser):
        serializer = LikeArticleSerializer(data=request.data)
        article = Article.objects.filter(id=idArticle)
        article_is_exist = article.count()

        objects_like = LikeArticle.objects.filter(id_user=request.user, id_article=idArticle)
        like_is_exist = objects_like.count()

        if article_is_exist > 0:
            if serializer.is_valid():
                ManageNotification().create_notification(request.user, pseudoUser, 2)

                if like_is_exist > 0:
                    objects_like.delete()
                    serializer.save(id_article=article[0], id_user=request.user)

                else:
                    serializer.save(id_article=article[0], id_user=request.user)

                LikeArticle.nbs_likes = {i+1: LikeArticle.objects.filter(
                    id_article=idArticle,
                    reaction=i+1
                ).count()for i in range(3)}
                return Response(serializer.data)

            else:
                return Response(
                    " ERROR : serialiazer pas valid ",
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                " ERROR : l'article n'existe pas ",
                status=status.HTTP_400_BAD_REQUEST
            )


""" Manage endpoint's post article """


class CreateArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        serializer = ArticleCreateSerailizer(data=request.data)
        id_category = request.data.get('id_category', '')
        category = Categories.objects.get(id=id_category)

        if serializer.is_valid():
            Article.info_user = {
                "image_profile": str(CustomUser.objects.get(pk=1).image_profile),
                "pseudo": request.user.username
            }
            serializer.save(
                id_user=request.user,
                date_article=timezone.now(),
                id_category=category,
            )

            return Response(serializer.data)
        else:
            return Response(
                    " ERROR : serialiazer pas valid ",
                    status=status.HTTP_400_BAD_REQUEST
                )


""" Manage endpoint's list's user article """


class ListArticlesUser(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, idUser):
        articles_user = Article.objects.filter(id=idUser)
        serializer = AllDataArticle().get_all_infos(articles_user)

        return Response(serializer.data)


""" Manage endpoint's list's categories """


class ListCategories(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)
