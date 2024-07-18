from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views_count += 1
        article.save()
        return article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        if form.is_valid():
            article = form.save()
            article.slug = slugify(article.title)
            article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.object.pk])


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:articles')

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.object.pk])


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
