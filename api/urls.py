from django.urls import path, include

urlpatterns = [
    path('articles/', include('api_articles.urls')),
    path('comments/', include('api_comments.urls')),
    path('user/', include('api_user.urls')),
    path('notification/', include('api_notification.urls')),
]
