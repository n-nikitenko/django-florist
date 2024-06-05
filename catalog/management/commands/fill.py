import os
from json import load
from pprint import pprint

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    path: str

    def __init__(self):
        super().__init__()
        self.path = os.path.join(BASE_DIR, "fixtures", "catalog_data.json")

    def json_read_categories(self):
        """Здесь мы получаем данные из фикстур с категориями"""
        categories = {}
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = load(f)
                for d in data:
                    if d['model'] == 'catalog.category':
                        categories[d['pk']] = Category(title=d['fields']['title'],
                                                       description=d['fields'].get('description'))
        except FileNotFoundError as e:
            print(e)

        return categories

    def json_read_products(self):
        """Здесь мы получаем данные из фикстур с продуктами"""
        products = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = load(f)
                for d in data:
                    if d['model'] == 'catalog.product':
                        products.append(Product(title=d['fields']['title'],
                                                description=d['fields'].get('description'),
                                                preview=d['fields'].get('preview'),
                                                price=d['fields'].get('price'),
                                                category_id=d['fields'].get('category')
                                                ))
        except FileNotFoundError as e:
            print(e)
        return products

    def handle(self, *args, **options):
        """Заполнение таблиц категорий и продуктов из фикстур"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_dict = self.json_read_categories()
        products_for_create = self.json_read_products()

        categories_for_create = categories_dict.values()

        created_categories = Category.objects.bulk_create(categories_for_create)
        id_category_map = {}
        # запоминаем новые pk категорий
        for category in created_categories:
            id_category_map[list(categories_dict.keys())[list(categories_dict.values()).index(category)]] = category

        # обновляем ссылки на категории в products
        for product in products_for_create:
            if id_category_map.get(product.category_id):
                product.category = id_category_map[product.category_id]

        Product.objects.bulk_create(products_for_create)
