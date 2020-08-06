from django.http import HttpResponse
from django.views.generic import TemplateView



# Create your views here.
class HomeViews(TemplateView):
    template_name = template_name = "user/home.html"

class MyAccountView(TemplateView):
    template_name = "user/myaccount.html"

class ConnexionView(TemplateView):
    template_name = "user/connexion.html"

class SearchUserView(TemplateView):
    template_name = "user/search_user.html"

class NotificationsView(TemplateView):
    template_name = "user/notifications.html"

class ParameterAccountView(TemplateView):
    template_name = "user/ParameterAccount.html"
