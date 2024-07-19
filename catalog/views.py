from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory, BaseFormSet
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Contacts, Version
from catalog.forms import ProductForm, VersionForm, BaseVersionFormSet, ModeratorProductForm


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


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = 'products'
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:thanks')

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.creator = self.request.user
            product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product

    def get_form_class(self):
        user = self.request.user
        if user.is_moderator:
            return ModeratorProductForm
        if user == self.object.creator:
            return ProductForm
        raise PermissionDenied

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        if self.request.user.is_moderator:
            return context_data
        if 'formset' in kwargs:
            context_data['formset'] = kwargs['formset']
        else:
            VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1, formset=BaseVersionFormSet)
            if self.request.method == 'POST':
                context_data['formset'] = VersionFormset(self.request.POST, self.request.FILES, instance=self.object)
            elif self.request.method == 'GET':
                context_data['formset'] = VersionFormset(instance=self.object)
        context_data['errors'] = context_data['formset'].non_form_errors()
        return context_data

    def form_valid(self, form):
        if self.request.user.is_moderator:
            return super().form_valid(form)
        context_data = self.get_context_data()
        formset = context_data.get('formset')
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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
