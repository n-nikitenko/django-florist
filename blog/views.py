from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 2


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views_count += 1
        article.save()
        return article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:articles')

    def form_valid(self, form):
        if form.is_valid():
            article = form.save()
            article.slug = slugify(article.title)
            article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:articles')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
