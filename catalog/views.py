from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Contacts
from catalog.forms import ProductForm


def home(request):
    last_five_products = Product.objects.all().order_by('-created_at')[:5]
    for product in last_five_products:
        print(product)
    return render(request, 'catalog/index.html')


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Contacts.objects.all()
        context["title"] = 'contacts'
        return context

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        message = self.request.POST.get('content')
        print(f'You have new message from {name}({email}): {message}')
        return HttpResponse('OK')


def services(request):
    return render(request, 'catalog/services.html', context={'title': 'services'})


class ProductListView(ListView):
    model = Product
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:thanks')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:prices')


def gallery(request):
    return render(request, 'catalog/gallery.html', context={'title': 'gallery'})


def about(request):
    return render(request, 'catalog/about.html', context={'title': 'about us'})


def not_found(request):
    return render(request, 'catalog/404.html', context={'title': '404'})


def thanks(request):
    return render(request, 'catalog/thanks.html')
