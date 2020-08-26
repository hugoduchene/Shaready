from django.urls import  path
from articles.views import FeedViews, ArticlesOnlyViews

urlpatterns = [
    path('', FeedViews.as_view(), name="feed"),
    path('<int:id_article>', ArticlesOnlyViews.as_view(), name="only_article")
]
