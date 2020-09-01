from django.core.management.base import BaseCommand
from articles.models import Article

""" Command to delete all articles """


class Command(BaseCommand):
    help = ""

    def handle(self, *arg, **options):
        all_articles = Article.objects.all()
        all_articles.delete()
