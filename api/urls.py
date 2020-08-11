from django.urls import path, include

urlpatterns = [
    path('articles/', include('api_articles.urls')),
    path('comments/', include('api_comments.urls')),
]
