from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import home, services, gallery, about, not_found, thanks, \
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView, \
    CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', services, name='services'),
    path('products/', ProductListView.as_view(extra_context={'title': 'products'}), name='products'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('products/<int:pk>/edit/', never_cache(ProductUpdateView.as_view()), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/',  CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_view'),
    path('about/', about, name='about'),
    path('404/', not_found, name='404'),
    path('new_product/', never_cache(ProductCreateView.as_view()), name='new_product'),
    path('thanks/', thanks, name='thanks')
]
