from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product, Contacts


# Create your views here.

def home(request):
    last_five_products = Product.objects.all().order_by('-created_at')[:5]
    for product in last_five_products:
        print(product)
    return render(request, 'catalog/index.html')


def contacts(request):
    data = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('content')
        print(f'You have new message from {name}({email}): {message}')
        return HttpResponse('OK')
    return render(request, 'catalog/contacts.html', context={'data': list(data), 'title': 'contacts'})


def services(request):
    return render(request, 'catalog/services.html', context={'title': 'services'})


def prices(request):
    products = Product.objects.all()
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/prices.html', context={'title': 'prices', "page_obj": page_obj})


def product(request, pk: int):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/product.html', context={'product': product, 'title': 'prices'})


def gallery(request):
    return render(request, 'catalog/gallery.html', context={'title': 'gallery'})


def about(request):
    return render(request, 'catalog/about.html', context={'title': 'about us'})


def not_found(request):
    return render(request, 'catalog/404.html', context={'title': '404'})
