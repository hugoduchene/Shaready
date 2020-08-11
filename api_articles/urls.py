from django.urls import  path
from api_articles.views import (
    ListArticlesUser,
    ListCategories,
    CreateArticle,
    CreateLikeArticle,
    GetArticleCategory,
    GetArticleTrends,
)

urlpatterns = [
    path('getTrends/', GetArticleTrends.as_view(), name="trends"),
    path('getArticleCategory/<int:idCategory>/<int:idPage>', GetArticleCategory.as_view(), name="list_artcile_category"),
    path('postLikeArticle/<int:idArticle>', CreateLikeArticle.as_view() , name="create_like_article"),
    path('postCreateArticle', CreateArticle.as_view(), name="create_article"),
    path('getArticleUser/<int:idUser>', ListArticlesUser.as_view(), name="list_article_user"),
    path('categories/', ListCategories.as_view(), name="categories_api"),
]
