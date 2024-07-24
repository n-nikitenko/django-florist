from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', ArticleListView.as_view(extra_context={'title': 'blog'}), name='articles'),
    path('blog/article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('blog/article/create/', never_cache(ArticleCreateView.as_view()), name='create_article'),
    path('blog/article/<int:pk>/edit/', never_cache(ArticleUpdateView.as_view()), name='edit_article'),
    path('blog/article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
]
