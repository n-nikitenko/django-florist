from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, services, gallery, about, not_found, thanks, \
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', services, name='services'),
    path('prices/', ProductListView.as_view(extra_context={'title': 'prices'}), name='prices'),
    path('prices/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('prices/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('prices/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('404/', not_found, name='404'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),
    path('thanks/', thanks, name='thanks')
]
