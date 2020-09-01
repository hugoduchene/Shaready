from django.core.paginator import Paginator
from rest_framework import status
from utils.all_data_comment import AllDataComment
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.notification import ManageNotification
from articles.models import Article, Comment, LikeComment
from user.models import CustomUser
from rest_framework.renderers import JSONRenderer
from api_comments.serializer import (
    CommentArticleSerializer,
    LikeCommentSerializer,
)

""" Manage endpoint's comment """


class GetAllCommentArticle(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, idArticle, idPage):
        all_comments = Comment.objects.filter(id_article=idArticle).order_by('-date_comment', 'likecomment')
        pagination = Paginator(all_comments, 10)
        objects_page = pagination.page(idPage).object_list
        serializer = AllDataComment().get_all_infos_comment(objects_page)

        return Response(serializer.data)


""" Manage endpoint's like's comment """


class CreateLikeCommentArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, idComment, pseudoUser):
        comment = Comment.objects.filter(pk=idComment)
        comment_is_exist = comment.count()

        like_user = LikeComment.objects.filter(
            id_user=request.user,
            id_comments=idComment
        )

        like_is_exit = like_user.count()

        if comment_is_exist > 0:
            serializer = LikeCommentSerializer(data=request.data)
            if serializer.is_valid():
                ManageNotification().create_notification(request.user, pseudoUser, 3)

                if like_is_exit > 0:
                    like_user.delete()

                serializer.save(id_comments=comment[0], id_user=request.user)
                LikeComment.nbs_likes = {
                    1: LikeComment.objects.filter(id_comments=idComment, reaction_comment=1).count(),
                    2: LikeComment.objects.filter(id_comments=idComment, reaction_comment=2).count(),
                }
                return Response(serializer.data)
            else:
                return Response(
                    "ERROR : serialiazer pas valide",
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    "ERROR : le commentaire n'existe pas",
                    status=status.HTTP_400_BAD_REQUEST
                )


class CreateCommentArticle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, idArticle, pseudoUser):
        article = Article.objects.filter(id=idArticle)
        article_is_exist = article.count()

        if article_is_exist == 1:
            serializer = CommentArticleSerializer(data=request.data)
            ManageNotification().create_notification(request.user, pseudoUser, 4)

            if serializer.is_valid(raise_exception=True):
                Comment.info_user = {
                    "id_user_comment": request.user.id,
                    "image_profile": str(CustomUser.objects.get(pk=request.user.id).image_profile),
                    "pseudo": request.user.username,
                    "date": timezone.now()
                }
                serializer.save(id_article=article[0], id_user=request.user, date_comment=timezone.now())
                return Response(serializer.data)

        return Response(
                    "ERROR : le commentaire n'existe pas",
                    status=status.HTTP_400_BAD_REQUEST
                )
