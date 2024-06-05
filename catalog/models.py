from django.db import models


class Category(models.Model):
    title = models.TextField(verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    created_at = models.DateTimeField(verbose_name='Дата/время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата/время обновления', auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.TextField(verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    preview = models.ImageField(null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    created_at = models.DateTimeField(verbose_name='Дата/время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата/время обновления', auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contacts(models.Model):
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    email = models.EmailField(null=True, verbose_name="E-mail")

    def __str__(self):
        return f"{self.address}\nТелефон: {self.phone}\nE-mail: {self.email}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
