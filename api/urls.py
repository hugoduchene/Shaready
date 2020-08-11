from django.urls import path, include

urlpatterns = [
    path('articles/', include('api_articles.urls')),
    
]
