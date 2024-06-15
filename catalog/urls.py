from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, services, prices, gallery, about, not_found, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name=app_name),
    path('contacts/', contacts, name=app_name),
    path('services/', services, name=app_name),
    path('prices/', prices, name=app_name),
    path('prices/<int:pk>', product, name=app_name),
    path('gallery/', gallery, name=app_name),
    path('about/', about, name=app_name),
    path('404/', not_found, name=app_name),
]
