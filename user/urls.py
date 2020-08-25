from django.urls import  path
from django.contrib.auth import views as auth_views
from user.views import (
    MyAccountView, 
    ConnexionView, 
    SearchUserView, 
    NotificationsView,
    ParameterAccountView,
    AccountView,
    LegalNoticeView,
)

urlpatterns = [
    path('myaccount/<int:id_account>', MyAccountView.as_view()),
    path('account/<int:id_account>', AccountView.as_view()),
    path('login', ConnexionView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    path('search', SearchUserView.as_view()),
    path('notifications', NotificationsView.as_view()),
    path('account/parameter', ParameterAccountView.as_view()),
    path('cgu/legalnotice', LegalNoticeView.as_view()),
]
