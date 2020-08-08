from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.base import View
from user.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout




# Create your views here.
class HomeViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, "user/home.html", context={'form' : RegistrationForm})
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password1)
                login(request, user)
                
                return redirect("feed")
        return render(request, "user/home.html")
    
            
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
