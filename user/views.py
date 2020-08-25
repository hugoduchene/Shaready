import base64
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.base import View
from user.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser, Subscription
from user.forms import ChangePictureForm, CustomUserForms
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile

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
        return render(request, "user/home.html", context={'form' : form})
    
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

class ParameterAccountView(View):
    def post(self, request, *args, **Kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        form = ChangePictureForm(request.POST, request.FILES, instance=user)

        img_data = request.POST.get('cropped_img')
        format, imgstr = img_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr)) 
        if user.image_profile != "user-default.png":
            user.image_profile.delete(save=True) 
        file_name = str(user.id) + '_' + str(user.username) + '.' + ext
        user.image_profile.save(file_name, data, save=True) 
        
        return render(request, "user/ParameterAccount.html", context={
            "form" : form,
        })
        
    def get(self, request, *args, **Kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        form = ChangePictureForm(instance=user)
        return render(request, "user/ParameterAccount.html", context={
            "form" : form,
        })

class ConnexionView(LoginView):
    template_name = "user/login.html"
    authentication_form = CustomUserForms

class SearchUserView(TemplateView):
    template_name = "user/search_user.html"

class NotificationsView(TemplateView):
    template_name = "user/notifications.html"

class LegalNoticeView(TemplateView):
    template_name = "cgu/legalnotice.html"


