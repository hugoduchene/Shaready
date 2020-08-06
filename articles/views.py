from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class FeedViews(TemplateView):
    template_name = "articles/feed.html"

class ArticlesOnlyViews(TemplateView):
    template_name = "articles/articles_only.html"
