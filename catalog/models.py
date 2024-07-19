from django.db import models

from users.models import User


class Category(models.Model):
    title = models.TextField(verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    created_at = models.DateTimeField(
        verbose_name="Дата/время создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата/время обновления", auto_now=True
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.TextField(
        verbose_name="Наименование", help_text="Введите наименование товара"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(verbose_name="Изображение")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Укажите цену товара",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата/время создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата/время обновления", auto_now=True
    )

    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")

    def __str__(self):
        return f"{self.title}"

    @property
    def active_version(self):
        return self.versions.filter(is_current=True).first()

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Создатель",
                                related_name="user_products")

    class Meta:
        verbose_name = "Продукт"
        ordering = ["created_at"]
        verbose_name_plural = "Продукты"
        permissions = [
            ('can_change_description', 'может менять описание'),
            ('can_change_category', 'может менять категорию'),
            ('can_change_is_published', 'может менять признак публикации')
        ]


class Contacts(models.Model):
    address = models.TextField(verbose_name="Адрес", help_text="Введите адрес")
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Телефон"
    )
    email = models.EmailField(null=True, verbose_name="E-mail")

    def __str__(self):
        return f"{self.address}\nТелефон: {self.phone}\nE-mail: {self.email}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        related_name="versions",
    )
    number = models.CharField(
        max_length=20, verbose_name="Номер версии", help_text="Укажите номер версии"
    )
    title = models.TextField(
        verbose_name="Название версии",
        blank=True,
        null=True,
        help_text="Введите название версии",
    )
    is_current = models.BooleanField(
        default=False, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
