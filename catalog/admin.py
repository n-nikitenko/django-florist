from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'title', 'is_current')
    list_filter = ('product', 'number', 'title', 'is_current')
    search_fields = ('product', 'number', 'title', 'is_current')
