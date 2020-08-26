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
    path('myaccount/<int:id_account>', MyAccountView.as_view(), name="myaccount"),
    path('account/<int:id_account>', AccountView.as_view(), name="account"),
    path('login', ConnexionView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    path('search', SearchUserView.as_view(), name="search"),
    path('notifications', NotificationsView.as_view()),
    path('account/parameter', ParameterAccountView.as_view(), name="parameter"),
    path('cgu/legalnotice', LegalNoticeView.as_view(), name="legal_notice"),
]
