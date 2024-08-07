from catalog.models import Category
from config import settings
from django.core.cache import cache


def get_categories_from_cache():
    """сервисная функция, отвечающая за выборку категорий из кеша или БД"""

    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list
