import os

from django.core import management
from django.core.management import BaseCommand
from django.core.management.commands import loaddata

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    path: str

    def __init__(self):
        super().__init__()
        self.path = os.path.join(BASE_DIR, "fixtures", "catalog_data.json")

    def handle(self, *args, **options):
        """Заполнение таблиц категорий и продуктов из фикстур"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        management.call_command(loaddata.Command(), self.path, verbosity=0)
