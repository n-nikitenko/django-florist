import os
from json import load
from pprint import pprint

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR
from django.core import management
from django.core.management.commands import loaddata


class Command(BaseCommand):
    path: str

    def __init__(self):
        super().__init__()
        self.path = os.path.join(BASE_DIR, "fixtures", "catalog_data.json")

    def handle(self, *args, **options):
        """Заполнение таблиц категорий и продуктов из фикстур"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        management.call_command('loaddata', self.path, verbosity=0)
