from django.test import TestCase
from articles.models import Categories
from articles.management.commands.create_categories import Command

""" unit test on command """


class TestCommandCreateCategories(TestCase):

    def setUp(self):
        self.command = Command()
        self.list_categories = self.list_categories = [
            'Political',
            'Economy',
            'Computer Science',
            'Video games',
            'Poetry',
            'Story time',
            'Social Network',
            'Shaready',
        ]

    def test_verify_is_exist_without_objects(self):
        self.command.verify_is_exist()
        self.assertEquals(self.list_categories, self.command.list_categories)

    def test_verify_is_exist_with_objects(self):
        list_categories_with_objects = [
            '',
            'Economy',
            'Computer Science',
            'Video games',
            'Poetry',
            'Story time',
            'Social Network',
            'Shaready',
        ]
        Categories(name_category='Political').save()
        self.command.verify_is_exist()

        self.assertEquals(self.command.list_categories, list_categories_with_objects)

    def test_insert_category(self):
        self.command.verify_is_exist()
        self.command.insert_category()
        length_table = Categories.objects.all().count()

        self.assertEquals(length_table, len(self.command.list_categories))

