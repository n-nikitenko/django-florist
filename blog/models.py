from django.db import models

from blog.utils import send_congratulations


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=200, null=True, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(null=True, verbose_name="Изображение")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="Кол-во просмотров")

    created_at = models.DateTimeField(verbose_name='Дата/время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата/время обновления', auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        if self.views_count == 100:
            send_congratulations(self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
