from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.base import View
from user.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser, Subscription
from user.forms import ChangePictureForm

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
    
class AccountView(View):
    def get(self, request, id_account, *args, **Kwargs) :
        infos_user = CustomUser.objects.get(pk=id_account)
        nbs_follows = infos_user.user_receiving_follow.count()
        nbs_gold_likes = infos_user.likearticle_set.filter(reaction=1).count()
        current_sub = Subscription.objects.filter(
            id_giving = request.user,
            id_receiving = id_account,
        ).count()
        return render(request, "user/account.html", context={
            'infos_user' : infos_user,
            'nbs_follow' :  nbs_follows,
            'nbs_gold_like' : nbs_gold_likes,
            'current_sub' : current_sub,
        })          

class MyAccountView(View):
    def get(self, request, id_account, *args, **Kwargs):
        if request.user.id == id_account:
            nbs_follows = request.user.user_receiving_follow.count()
            nbs_gold_likes = request.user.likearticle_set.filter(reaction=1).count()
            current_sub = Subscription.objects.filter(
                id_giving = request.user,
                id_receiving = id_account,
            ).count()
            return render(request, "user/myaccount.html", context={
                'nbs_follow' :  nbs_follows,
                'nbs_gold_like' : nbs_gold_likes,
                'current_sub' : current_sub,
            })
        else:
            return redirect('feed')

class ConnexionView(TemplateView):
    template_name = "user/connexion.html"

class SearchUserView(TemplateView):
    template_name = "user/search_user.html"

class NotificationsView(TemplateView):
    template_name = "user/notifications.html"

class ParameterAccountView(View):
    def post(self, request, *args, **Kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        form = ChangePictureForm(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            form.save()
            return render(request, "user/ParameterAccount.html", context={
                "form" : form,
            })
        
    def get(self, request, *args, **Kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        form = ChangePictureForm(instance=user)
        return render(request, "user/ParameterAccount.html", context={
            "form" : form,
        })
