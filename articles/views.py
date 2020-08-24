from django.shortcuts import render
from django.views.generic import TemplateView, View
from articles.models import Article, Categories

# Create your views here.

class FeedViews(View):
    
    def get(self, request, *args, **Kwargs):
        all_categories = Categories.objects.all()

        return render(request, "articles/feed.html", context={
            "categories" : all_categories
        })


class ArticlesOnlyViews(View):
    
    def get(self, request, id_article, *args, **Kwargs):
        article = Article.objects.get(pk=id_article)
        info_user = article.id_user
        nbs_like = {i : article.likearticle_set.filter(reaction=i).count() for i in range(1,4)}
        nbs_comments = article.comment_set.count()
        
        return render(request, "articles/articles_only.html",context={
            "info_user" : info_user,
            "nbs_like" : nbs_like,
            "article" : article,
            "nbs_comments" : nbs_comments
        })



