from django.shortcuts import render
from django.views.generic import TemplateView, View
from articles.models import Article

# Create your views here.

class FeedViews(TemplateView):
    template_name = "articles/feed.html"

class ArticlesOnlyViews(View):
    
    def get(self, request, id_article, *args, **Kwargs):
        article = Article.objects.get(pk=id_article)
        info_user = article.id_user
        nbs_like = {i : article.likearticle_set.filter(reaction=i).count() for i in range(1,5)}


        return render(request, "articles/articles_only.html",context={
            "info_user" : info_user,
            "nbs_like" : nbs_like,
            "article" : article,
        })



