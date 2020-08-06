from django.urls import  path
from user.views import (
    MyAccountView, 
    ConnexionView, 
    SearchUserView, 
    NotificationsView,
    ParameterAccountView)

urlpatterns = [
    path('account/<int:id_account>', MyAccountView.as_view()),
    path('login', ConnexionView.as_view()),
    path('search', SearchUserView.as_view()),
    path('notifications', NotificationsView.as_view()),
    path('account/<int:id_account>/parameter', ParameterAccountView.as_view()),
]
