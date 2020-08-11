from django.core.paginator import Paginator
from api_comments.utils.all_data_comment import AllDataComment
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article, Comment, LikeComment
from api_comments.serializer import (
    CommentArticleSerializer,
    LikeCommentSerializer,
)

""" Manage endpoint's comment """

class GetAllCommentArticle(APIView):

    def get(self, request, idArticle, idPage):
        all_comments = Comment.objects.filter(id=idArticle).order_by('-date_comment')
        pagination = Paginator(all_comments, 10)
        objects_page = pagination.get_page(idPage).object_list
        serializer = AllDataComment().get_all_infos_comment(objects_page)

        return Response(serializer.data)

class CreateLikeCommentArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, idComment):
        comment = Comment.objects.filter(id=idComment)
        comment_is_exist = comment.count()

        like_user = LikeComment.objects.filter(
            id_user=request.user, 
            id_comments=idComment
        )

        like_is_exit = like_user.count()

        if comment_is_exist > 0:
            serializer = LikeCommentSerializer(data=request.data)
            if serializer.is_valid():
                if like_is_exit > 0:
                    like_user.delete()
                    serializer.save(id_comments=comment[0], id_user=request.user)
                    return Response(serializer.data)
                else:
                    serializer.save(id_comments=comment[0], id_user=request.user)
                    return Response(serializer.data)
            else:
                return Response("ERROR SERIALIZER")
        else:
            return Response("ERROR")


class CreateCommentArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, idArticle):
        article = Article.objects.filter(id=idArticle)
        article_is_exist = article.count()

        if article_is_exist == 1:
            serializer = CommentArticleSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save(id_article=article, id_user=request.user, date_comment=timezone.now())
                return Response(serializer.data)
            return Response("ERROR")
        return Response("Cet article n'existe pas")
