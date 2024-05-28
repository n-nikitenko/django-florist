from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('content')
        print(f'You have new message from {name}({email}): {message}')
        return HttpResponse('OK')
    return render(request, 'catalog/contacts.html')


def services(request):
    return render(request, 'catalog/services.html')


def prices(request):
    return render(request, 'catalog/prices.html')


def gallery(request):
    return render(request, 'catalog/gallery.html')


def about(request):
    return render(request, 'catalog/about.html')


def not_found(request):
    return render(request, 'catalog/404.html')
