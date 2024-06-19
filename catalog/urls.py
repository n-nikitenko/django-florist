from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, services, prices, gallery, about, not_found, product, new_product, thanks

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('prices/', prices, name='prices'),
    path('prices/<int:pk>', product, name='product_view'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('404/', not_found, name='404'),
    path('new_product/', new_product, name='new_product'),
    path('thanks/', thanks, name='thanks')
]
