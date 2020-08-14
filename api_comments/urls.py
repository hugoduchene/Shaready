from django.urls import path, include
from api_comments.views import (
    GetAllCommentArticle,
    CreateLikeCommentArticle,
    CreateCommentArticle,
)

urlpatterns = [
   path('getAll/<int:idArticle>/<int:idPage>', GetAllCommentArticle.as_view(), name="getAll"),
   path('createLike/<int:idComment>', CreateLikeCommentArticle.as_view(), name="create_like_comment"),
   path('CreateComment/<int:idArticle>', CreateCommentArticle.as_view(), name="Create_comment")
]