import base64
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.base import View
from user.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from user.models import CustomUser, Subscription
from user.forms import ChangePictureForm, CustomUserForms
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile
from articles.models import Article, LikeArticle

# Create your views here.

""" Manages home view """


class HomeViews(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('feed')
        else:
            return render(request, "user/home.html", context={'form': RegistrationForm})

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
        return render(request, "user/home.html", context={'form': form})


""" Manages account view """


class AccountView(View):
    def get(self, request, id_account, *args, **Kwargs):
        if request.user.is_authenticated:
            infos_user = CustomUser.objects.get(pk=id_account)
            nbs_follows = infos_user.user_receiving_follow.count()
            nbs_gold_likes = infos_user.likearticle_set.filter(reaction=1).count()
            current_sub = Subscription.objects.filter(
                id_giving=request.user,
                id_receiving=id_account,
            ).count()
            return render(request, "user/account.html", context={
                'infos_user': infos_user,
                'nbs_follow':  nbs_follows,
                'nbs_gold_like': nbs_gold_likes,
                'current_sub': current_sub,
            })
        else:
            return redirect('home')


""" Manages myaccount view """


class MyAccountView(View):
    def get(self, request, id_account, *args, **Kwargs):
        if request.user.is_authenticated:
            if request.user.id == id_account:
                nbs_follows = request.user.user_receiving_follow.count()
                article_user = Article.objects.filter(id_user=request.user)
                nbs_gold_likes = LikeArticle.objects.filter(id_article__in=article_user, reaction=1).count()
                current_sub = Subscription.objects.filter(
                    id_giving=request.user,
                    id_receiving=id_account,
                ).count()
                return render(request, "user/myaccount.html", context={
                    'nbs_follow':  nbs_follows,
                    'nbs_gold_like': nbs_gold_likes,
                    'current_sub': current_sub,
                })
            else:
                return redirect('/user/account/' + str(id_account))
        else:
            return redirect('home')


""" Manages parameter account view """


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
            "form": form,
        })

    def get(self, request, *args, **Kwargs):
        if request.user.is_authenticated:
            user = CustomUser.objects.get(pk=request.user.id)
            form = ChangePictureForm(instance=user)
            return render(request, "user/ParameterAccount.html", context={
                "form": form,
            })
        else:
            return redirect('home')


""" Manages connexion view """


class ConnexionView(LoginView):
    template_name = "user/login.html"
    authentication_form = CustomUserForms


""" Manages search view """


class SearchUserView(View):

    def get(self, request, *args, **Kwargs):
        if request.user.is_authenticated:
            return render(request, "user/search_user.html")
        return redirect('home')


""" Manages notification view """


class NotificationsView(View):

    def get(self, request, *args, **Kwargs):
        if request.user.is_authenticated:
            return render(request, "user/notifications.html")
        else:
            return redirect('home')


""" Manages lagal notice view """


class LegalNoticeView(TemplateView):
    template_name = "cgu/legalnotice.html"
