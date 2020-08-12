from django.urls import  path
from api_articles.views import (
    ListArticlesUser,
    ListCategories,
    CreateArticle,
    CreateLikeArticle,
    GetArticleCategory,
    GetArticleTrends,
    GetArticleUser,
)

urlpatterns = [
    path('getarticleuser/<int:idUser>/<int:idPage>', GetArticleUser.as_view(), name="article_user"),
    path('gettrends/', GetArticleTrends.as_view(), name="trends"),
    path('getarticlecategory/<int:idCategory>/<int:idPage>', GetArticleCategory.as_view(), name="list_artcile_category"),
    path('postlikearticle/<int:idArticle>', CreateLikeArticle.as_view() , name="create_like_article"),
    path('postcreatearticle', CreateArticle.as_view(), name="create_article"),
    path('getarticleuser/<int:idUser>', ListArticlesUser.as_view(), name="list_article_user"),
    path('categories/', ListCategories.as_view(), name="categories_api"),
]
