from django.shortcuts import render, redirect
from django.views.generic import View
from articles.models import Article, Categories

# Create your views here.

""" Manages feed's views """


class FeedViews(View):

    def get(self, request, *args, **Kwargs):
        if request.user.is_authenticated:
            all_categories = Categories.objects.all().order_by('name_category')

            return render(request, "articles/feed.html", context={
                "categories": all_categories
            })
        else:
            return redirect('home')


""" Manages articles only views """


class ArticlesOnlyViews(View):

    def get(self, request, id_article, *args, **Kwargs):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=id_article)
            info_user = article.id_user
            nbs_like = {i: article.likearticle_set.filter(reaction=i).count() for i in range(1, 4)}
            nbs_comments = article.comment_set.count()

            return render(request, "articles/articles_only.html", context={
                "info_user": info_user,
                "nbs_like": nbs_like,
                "article": article,
                "nbs_comments": nbs_comments
            })
        else:
            return redirect('home')
