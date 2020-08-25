from django.core.management.base import BaseCommand
from articles.models import Categories

class Command(BaseCommand):
    help = ""
    
    """ When someone wants add a category he has to put it at the end of the list """ 
    def __init__(self):
        self.list_categories = [
            'Political', 
            'Economy',
            'Computer Science',
            'Video games',
            'Poetry',
            'Story time',
            'Social Network',
            'Shaready',
        ]
    
    def verify_is_exist(self):
        all_categories = Categories.objects.all()

        if all_categories.count() > 0:
            for i, category in enumerate(all_categories):
                if category.name_category == self.list_categories[i]:
                    self.list_categories[i] = ''
    
    def insert_category(self):
        for category in self.list_categories:
            if category != '':
                c = Categories(name_category=category)
                c.save()

    def handle(self, *arg, **options):
        self.verify_is_exist()
        self.insert_category()

    